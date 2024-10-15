{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    systems.url = "github:nix-systems/default";
    poetry2nix-flake.url = "github:nix-community/poetry2nix";
  };

  outputs = { nixpkgs, systems, poetry2nix-flake, self }:
    let
      pkgsFor = system: import nixpkgs { inherit system; };
      forEachSystem = f: nixpkgs.lib.genAttrs (import systems) (system:
        let
          pkgs = pkgsFor system;
          poetry2nix = import poetry2nix-flake { inherit pkgs; };
        in
        f { inherit system pkgs poetry2nix; });
    in
    {
      # Doesnt work: https://github.com/nix-community/poetry2nix/issues/555
      packages = forEachSystem ({ poetry2nix, ... }: {
        default = poetry2nix.mkPoetryApplication {
          projectDir = self;
        };
      });
      devShells = forEachSystem ({ pkgs, ... }: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            python312
            poetry
            just
          ];
          shellHook =
            let libPath = pkgs.lib.makeLibraryPath [ pkgs.libGL ];
            in ''
              python --version
              export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${libPath}"
            '';
        };
      });
      formatter = forEachSystem ({ pkgs, ... }: pkgs.nixpkgs-fmt);
    };
}
