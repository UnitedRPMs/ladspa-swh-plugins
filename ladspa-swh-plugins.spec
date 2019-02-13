%define pkgname swh-plugins

Summary:        A set of audio plugins for LADSPA
Name:           ladspa-%{pkgname}
Version:        0.4.17
Release:        2%{?dist}
License:        GPLv2+
URL:            http://plugin.org.uk/
Source0:        https://github.com/swh/ladspa/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Unbundle libgsm
Patch0:         ladspa-swh-plugins-libgsm.patch
# Do not add -march directives to CFLAGS
Patch1:         swh-plugins-0.4.17-riceitdown.patch
# Fix an undefined symbol due to a misplaced inline
Patch2:         swh-plugins-noinline.patch
# Add Language headers to the po files
Patch3:         swh-plugins-language.patch

BuildRequires:  fftw3-devel
BuildRequires:  gettext-devel
BuildRequires:  gsm-devel
BuildRequires:  ladspa-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig

Requires:       ladspa

%description
A set of audio plugins for LADSPA (see http://plugin.org.uk/ for more
details).

%prep
%setup -q -n ladspa-%{version}
%patch0
%patch1
%patch2
%patch3

%build
autoreconf -f -i
CFLAGS="$RPM_OPT_FLAGS -fPIC -DPIC" %configure --disable-static
make %{?_smp_mflags} static

%install
%make_install
%find_lang %{pkgname}

%files -f %{pkgname}.lang
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May  5 2018 Jerry James <loganjerry@gmail.com> - 0.4.17-1
- New upstream version
- Drop upstreamed patches: -Makefile.am, -Makefile.in, -fPIC, -pic
- Fix undefined symbol (bz 1506432)
- Add -language patch to add Language headers to po files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.4.15-26
- Fix undefined symbols RHBZ#1285020 thanks to Jerome Audu, Francesco Frassinelli
- Some SPEC file cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.15-15
- fix this package so it builds properly, with the right optflags, and without tons of missing symbols

* Thu Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.4.15-14
- make it build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.15-12
- Autorebuild for GCC 4.3

* Mon Oct 08 2007 Anthony Green <green@redhat.com> 0.4.15-11
- Bump release to fix tagging oops.

* Mon Oct 08 2007 Anthony Green <green@redhat.com> 0.4.15-9
- Use the system gsm library.
- Require ladspa to prevent orphaned directories.
- Add -fPIC -DPIC to CFLAGS.  Removed patch from rev -7.
- Update license tag.

* Sat Feb 03 2007 Anthony Green <green@redhat.com> 0.4.15-8
- BuildRequire libtool.

* Sat Feb 03 2007 Anthony Green <green@redhat.com> 0.4.15-7
- Remove SELinux bits and compile with fPIC instead.  
  See bugzilla 225060 and %%patch1.

* Sat Jan 06 2007 Anthony Green <green@redhat.com> 0.4.15-6
- Add SELinux bits for sc4m_1916.so.
- Add policycoreutils dependencies.

* Wed Dec 27 2006 Anthony Green <green@redhat.com> 0.4.15-5
- Rename package from swh-plugins.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.4.15-4
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 0.4.15-3
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com> 0.4.15-2.1
- Rebuild.

* Sun Sep 10 2006 Anthony Green <green@redhat.com> 0.4.15-2
- Add BuildRequires for pkgconfig.

* Sat Sep  9 2006 Anthony Green <green@redhat.com> 0.4.15-1
- Update sources.  Remove obsolete patch.

* Mon Apr 24 2006 Anthony Green <green@redhat.com> 0.4.14-3
- Add -configure patch.  Configure with --disable-static.

* Mon Apr 24 2006 Anthony Green <green@redhat.com> 0.4.14-2
- Fix Summary.
- Don't install INSTALL or the empty NEWS file.
- Remove some BuildRequirements.

* Sat Apr 22 2006 Anthony Green <green@redhat.com> 0.4.14-1
- Build for Fedora Extras.
- Use %%find_lang.
- Don't own the ladspa dir.

* Fri Jun 24 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.13
- removed ps_in and ps_out external declarations in pitchscale.h,
  otherwise build fails in fc4/gcc4
* Fri Mar 25 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.13-1
- updated to 0.4.13
* Mon Jan 24 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.12-1
- updated to 0.4.12
* Mon Dec 20 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>  
- spec file cleanup
* Mon Nov 15 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.11-1
- updated to 0.4.11
* Tue Jul 20 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.7-1
- updated to 0.4.7
- multiarch build, up optimization to original -O6
* Sun Jul  4 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.4-1
- updated to 0.4.4
* Fri May 14 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.3-3
- more buildrequires, fixed file list
- patch for gcc3.3 happiness
* Sat May  8 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added proper buildrequires
* Wed Feb 18 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.3-2
- changed name of ladspa package, do not depend on it explicitly
* Tue Dec  2 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.3-1
- updated to 0.4.3
* Sat Oct 11 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.2-2
- updated to snapshot of 2003-08-19, jackEq requires dj_eq_1901
* Mon Jun  2 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.2-1
- updated to 0.4.2
* Tue Apr  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-2
- rebuilt for newer version of fftw
* Tue Apr  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-1
- updated to 0.4.0
* Fri Mar  7 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.7-1
- updated to 0.3.7
* Mon Jan 13 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.6-1
- updated to 0.3.6... boy, this is movin fast :-)
* Fri Jan 10 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.5
- updated to 0.3.5... should have waited :-)
* Thu Jan  9 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.4
- updated to 0.3.4
* Fri Dec 06 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.3
- updated to 0.3.3
* Wed Dec 04 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.2
- updated to 0.3.2
* Fri Nov  1 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.0
- updated to 0.3.0
* Fri Sep 06 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- updated to 0.2.8
* Fri Jan 18 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- updated to 0.2.3
- changed to globbing of .so files
* Thu Aug 23 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added prefix, cleanup
