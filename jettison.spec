%global pkg_name jettison
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.3.3
Release:        4.12%{?dist}
Summary:        A JSON StAX implementation
License:        ASL 2.0
URL:            http://jettison.codehaus.org/
# svn export http://svn.codehaus.org/jettison/tags/jettison-1.3.3 jettison-1.3.3
# rm -rf jettison-1.3.3/trunk
# tar cvJf jettison-1.3.3.tar.xz jettison-1.3.3
Source0:        %{pkg_name}-%{version}.tar.xz
BuildArch:      noarch

# Change the POM to use the version of woodstox that we have available:
Patch0: %{pkg_name}-update-woodstox-version.patch

%if 0%{?rhel} <= 5
%else
%endif
BuildRequires:     %{?scl_prefix_java_common}javapackages-tools
BuildRequires:     %{?scl_prefix_java_common}maven-local
BuildRequires:     %{?scl_prefix}maven-compiler-plugin
BuildRequires:     %{?scl_prefix}maven-install-plugin
BuildRequires:     %{?scl_prefix}maven-jar-plugin
BuildRequires:     %{?scl_prefix}maven-javadoc-plugin
BuildRequires:     %{?scl_prefix}maven-release-plugin
BuildRequires:     %{?scl_prefix}maven-resources-plugin
BuildRequires:     %{?scl_prefix}woodstox-core
BuildRequires:     %{?scl_prefix}stax2-api


%description
Jettison is a collection of Java APIs (like STaX and DOM) which read
and write JSON. This allows nearly transparent enablement of JSON based
web services in services frameworks like CXF or XML serialization
frameworks like XStream.


%package javadoc
Summary:           Javadocs for %{pkg_name}
Requires:          %{name} = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%patch0 -p1
# We don't need wagon-webdav
%pom_xpath_remove pom:build/pom:extensions

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# Disable the tests until BZ#796739 is fixed:
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc src/main/resources/META-INF/LICENSE


%files javadoc -f .mfiles-javadoc
%doc src/main/resources/META-INF/LICENSE


%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.3.3-4.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.3.3-4.11
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.3.3-4.10
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.3.3-4.9
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.3.3-4.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.3-4.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.3-4.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.3-4.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.3-4.4
- Remove requires on java

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.3.3-4.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.3-4.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.3-4.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3.3-4
- Mass rebuild 2013-12-27

* Tue Aug 27 2013 Michal Srb <msrb@redhat.com> - 1.3.3-3
- Migrate away from mvn-rpmbuild (Resolves: #997464)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.3-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Mar  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.3-1
- Check woodstox version patch into SCM
- Upload jettison-1.3.3.tar.xz

* Fri Mar 08 2013 David Xie <david.scriptfan@gmail.com> - 1.3.3-1
- Update to v1.3.3

* Tue Feb 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-9
- Remove wagon-webdav build extension

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3.1-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Sep 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-6
- Install LICENSE file with javadoc package

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Juan Hernandez <juan.hernandez at redhat.com> - 1.3.1-4
- Make sure the maven dependencies map is created and added

* Thu Feb 23 2012 Juan Hernandez <juan.hernandez at redhat.com> - 1.3.1-3
- Use maven to build and add the POM to the package

* Sun Jan 15 2012 Sandro Mathys <red at fedoraproject.org> - 1.3.1-2
- Drop the requirement for java* >= 1.6.0 for EL <= 5

* Sun Jan 15 2012 Sandro Mathys <red at fedoraproject.org> - 1.3.1-1
- New upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 30 2011 Sandro Mathys <red at fedoraproject.org> - 1.3-1
- New upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 25 2010 Sandro Mathys <red at fedoraproject.org> - 1.2-1
- update to upstream 1.2

* Sun Jun 28 2009 Sandro Mathys <red at fedoraproject.org> - 1.1-1
- initial build
