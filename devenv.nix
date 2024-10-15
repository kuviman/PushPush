{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    version = "3.12";
    venv.enable = true;
    venv.requirements = ''
      pygame==2.6.1
      PyOpenGL==3.1.1a1
    '';
  };
}
