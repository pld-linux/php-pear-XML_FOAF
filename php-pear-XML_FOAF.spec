%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	XML_FOAF
Summary:	%{_pearname} - provides the ability to manipulate FOAF RDF/XML
Summary(pl.UTF-8):	%{_pearname} - przetwarzanie plików FOAF RDF/XML
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	575d9b2cb3de3d8d9e2db9041a434391
URL:		http://pear.php.net/package/XML_FOAF/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.0-0.b1
Requires:	php-pear-RDF
Requires:	php-pear-XML_Beautifier >= 0.2.2
Requires:	php-pear-XML_Tree >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_FOAF allows advanced users to create advanced FOAF files. The FOAF
Project can be found at <http://www.foaf-project.org/> -
XML_FOAF_Parser and XML_FOAF_Lite will follow before 1.0.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
XML_FOAF pozwala zaawansowanym użytkownikom tworzyć zaawansowane pliki
FOAF. Projekt FOAF znajduje się pod adresem
<http://www.foaf-project.org/>. XML_FOAF_Parser i XML_FOAF_Lite ukażą
się przed 1.0.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/FOAF

%{_examplesdir}/%{name}-%{version}
