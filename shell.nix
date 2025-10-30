let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python313.withPackages (ps: with ps; [
      beautifulsoup4
      markdownify
      pybase64
      argh
      requests
    ]))
  ];
}

