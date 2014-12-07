Summary:	Fonts for the GhostScript PostScript(TM) interpreter
Name:		ghostscript-fonts
Version:	8.11
Release:	25
License:	GPLv2
Group:		Publishing
Url:		http://sourceforge.net/projects/gs-fonts/
Source0:	http://heanet.dl.sourceforge.net/sourceforge/gs-fonts/ghostscript-fonts-other-6.0.tar.bz2
BuildArch:	noarch

%description
These fonts can be used by the GhostScript interpreter during text
rendering. They are in addition to the shared fonts between GhostScript
and X11.

%prep
%setup -q -c ghostscript-fonts-6.0

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/default/ghostscript/
cp fonts/* %{buildroot}/%{_datadir}/fonts/default/ghostscript

# Remove unneeded files
rm -f %{buildroot}/%{_datadir}/fonts/default/ghostscript/*.pfb
rm -f %{buildroot}/%{_datadir}/fonts/default/ghostscript/fonts.{dir,scale}

%files
%dir %{_datadir}/fonts/default/
%dir %{_datadir}/fonts/default/ghostscript/
%{_datadir}/fonts/default/ghostscript/*.pfa
%{_datadir}/fonts/default/ghostscript/*.afm
%{_datadir}/fonts/default/ghostscript/*.gsf
%{_datadir}/fonts/default/ghostscript/*.pfm

