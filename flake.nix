{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    systems.url = "github:nix-systems/default";
  };

  outputs = { nixpkgs, systems, self }:
    let
      pkgsFor = system: import nixpkgs { inherit system; };
      forEachSystem = f: nixpkgs.lib.genAttrs (import systems) (system:
        let pkgs = pkgsFor system;
        in f { inherit system pkgs; });
    in
    {
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
