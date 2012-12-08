Summary:	Fonts for the GhostScript PostScript(TM) interpreter
Name:		ghostscript-fonts
Version:	8.11
Release:	%mkrel 18
License:	GPL
Group:		Publishing
Url:		http://sourceforge.net/projects/gs-fonts/
Source:		http://heanet.dl.sourceforge.net/sourceforge/gs-fonts/ghostscript-fonts-other-6.0.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch

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

%files
%defattr(-,root,root,-)
%dir %_datadir/fonts/default/
%dir %_datadir/fonts/default/ghostscript/
%_datadir/fonts/default/ghostscript/*.pfa
%_datadir/fonts/default/ghostscript/*.afm
%_datadir/fonts/default/ghostscript/*.gsf
%_datadir/fonts/default/ghostscript/*.pfm


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 8.11-16mdv2011.0
+ Revision: 664829
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 8.11-15mdv2011.0
+ Revision: 605453
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 8.11-14mdv2010.1
+ Revision: 494166
- fc-cache is now called by an rpm filetrigger

* Thu Sep 24 2009 Olivier Blin <oblin@mandriva.com> 8.11-13mdv2010.0
+ Revision: 448398
- add bootstrap flag to be able to break build-dep loop (from Arnaud Patard)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 8.11-12mdv2010.0
+ Revision: 424876
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 8.11-11mdv2009.1
+ Revision: 351204
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 8.11-10mdv2009.0
+ Revision: 221070
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 8.11-9mdv2008.1
+ Revision: 150106
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 05 2007 Frederic Crozat <fcrozat@mandriva.com> 8.11-8mdv2008.0
+ Revision: 95577
- Do not own /usr/share/fonts (cause fontconfig cache problem)
- Call fontconfig correctly in scripts

* Tue May 15 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 8.11-7mdv2008.0
+ Revision: 27116
- Specfile cleanup: remote urw fonts stuff, as they are located at urw-fonts
  package.


* Tue Jan 09 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 8.11-6mdv2007.0
+ Revision: 106448
- Rebuild.
- Import ghostscript-fonts

* Mon Oct 17 2005 Stefan van der Eijk <stefan@eijk.nu> 8.11-5mdk
- add Requires(post): fontconfig
- %%mkrel

* Thu Feb 10 2005 Till Kamppeter <till@mandrakesoft.com> 8.11-4mdk
- Removed dangling symlink /usr/share/fonts/default/ghostscript/Fontmap

* Sat Jul 31 2004 Till Kamppeter <till@mandrakesoft.com> 8.11-3mdk
- Added post-install script to update the fontconfig database (thanks
  to Frederic Crozat).

* Fri May 07 2004 Till Kamppeter <till@mandrakesoft.com> 8.11-2mdk
- Corrected GhostScript version number.

* Thu Jan 29 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 8.11-1mdk
- Fixed URL.

