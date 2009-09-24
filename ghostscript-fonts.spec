Summary:	Fonts for the GhostScript PostScript(TM) interpreter
Name:		ghostscript-fonts
Version:	8.11
Release:	%mkrel 13
License:	GPL
Group:		Publishing
Url:		http://sourceforge.net/projects/gs-fonts/
Source:		http://heanet.dl.sourceforge.net/sourceforge/gs-fonts/ghostscript-fonts-other-6.0.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch

%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

%if !%{bootstrap}
Requires(post):	fontconfig
%endif

%description
These fonts can be used by the GhostScript interpreter during text
rendering. They are in addition to the shared fonts between GhostScript
and X11.

%prep
%setup -q -c ghostscript-fonts-6.0

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/default/ghostscript/
cp fonts/* %buildroot/%_datadir/fonts/default/ghostscript

# Remove unneeded files
rm -f %buildroot/%_datadir/fonts/default/ghostscript/*.pfb
rm -f %buildroot/%_datadir/fonts/default/ghostscript/fonts.{dir,scale}

%clean
rm -fr %buildroot


%post
%if !%{bootstrap}
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
%endif

%postun
%if !%{bootstrap}
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi
%endif

%files
%defattr(-,root,root,-)
%dir %_datadir/fonts/default/
%dir %_datadir/fonts/default/ghostscript/
%_datadir/fonts/default/ghostscript/*.pfa
%_datadir/fonts/default/ghostscript/*.afm
%_datadir/fonts/default/ghostscript/*.gsf
%_datadir/fonts/default/ghostscript/*.pfm
