Name: hunspell-eo
Summary: Esperanto hunspell dictionaries
Version: 1.0
Release: 0.7.dev%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/3377/1/1.0-dev.oxt
URL: http://extensions.services.openoffice.org/project/literumilo
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv3
BuildArch: noarch

Requires: hunspell

%description
Esperanto hunspell dictionaries.

%prep
%setup -q -c

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p literumilo.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/eo.dic
cp -p literumilo.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/eo.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-0.7.dev
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 09 2010 Caolan McNamara <caolanm@redhat.com> - 1.0-0.2.dev
- drop buildrequire

* Thu Dec 03 2009 Caolan McNamara <caolanm@redhat.com> - 1.0-0.1.dev
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20041129-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20041129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Caolan McNamara <caolanm@redhat.com> - 0.20041129-1
- initial version
