%define tarballname yaml

#====================================================================#

Name:       libyaml
Version:    0.1.7
Release:    5%{?dist}
Summary:    YAML 1.1 parser and emitter written in C

Group:      System Environment/Libraries
License:    MIT
URL:        http://pyyaml.org/
Source0:    http://pyyaml.org/download/libyaml/%{tarballname}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  LibYAML is a YAML parser and
emitter written in C.


%package devel
Summary:   Development files for LibYAML applications
Group:     Development/Libraries
Requires:  libyaml = %{version}-%{release}, pkgconfig


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use LibYAML.


%prep
%setup -q -n %{tarballname}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" install
rm -f %{buildroot}%{_libdir}/*.{la,a}

soname=$(readelf -d %{buildroot}%{_libdir}/libyaml.so | awk '$2 == "(SONAME)" {print $NF}' | tr -d '[]')
rm -f %{buildroot}%{_libdir}/libyaml.so
echo "INPUT($soname)" > %{buildroot}%{_libdir}/libyaml.so


%check
make check


%ldconfig_scriptlets


%files
%license LICENSE
%doc README
%{_libdir}/%{name}*.so.*


%files devel
%doc doc/html
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/yaml-0.1.pc
%{_includedir}/yaml.h


%changelog
* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-5
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 John Eckersberg <eck@redhat.com> - 0.1.7-1
- New upstream release 0.1.7 (RHBZ#1371154)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec  1 2014 John Eckersberg <eck@redhat.com> - 0.1.6-6
- Add patch for CVE-2014-9130 (RHBZ#1169371)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 0.1.6-4
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 John Eckersberg <jeckersb@redhat.com> - 0.1.6-2
- Work around ldconfig bug with libyaml.so (bz1082822)

* Wed Mar 26 2014 John Eckersberg <jeckersb@redhat.com> - 0.1.6-1
- New upstream release 0.1.6 (bz1081492)
- Fixes CVE-2014-2525 (bz1078083)

* Tue Feb  4 2014 John Eckersberg <jeckersb@redhat.com> - 0.1.5-1
- New upstream release 0.1.5 (bz1061087)
- Removed patches for CVE-2013-6393; they are included in 0.1.5
  upstream

* Wed Jan 29 2014 John Eckersberg <jeckersb@redhat.com> - 0.1.4-6
- Add patches for CVE-2013-6393 (bz1033990)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 John Eckersberg <jeckersb@redhat.com> - 0.1.4-1
- New upstream release 0.1.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 02 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.3-1
- New upstream release 0.1.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-4
- Minor tweaks to spec file
- Enable %%check section
- Thanks Gareth Armstrong <gareth.armstrong@hp.com>

* Tue Mar 3 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-3
- Remove static libraries

* Thu Feb 26 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-2
- Remove README and LICENSE from docs on -devel package
- Remove -static package and merge contents into the -devel package

* Wed Feb 25 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-1
- Initial packaging for Fedora
