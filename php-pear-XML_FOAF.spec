%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	FOAF
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides the ability to manipulate FOAF RDF/XML
Summary(pl):	%{_pearname} - przetwarzanie plików FOAF RDF/XML
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fc90f044ef01832ab9c4999b1325bd71
URL:		http://pear.php.net/package/XML_FOAF/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-XML_Tree >= 1.1
Requires:	php-pear-XML_Beautifier >= 0.2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_FOAF allows advanced users to create advanced FOAF files.
The FOAF Project can be found at http://www.foaf-project.org/ -
XML_FOAF_Parser and XML_FOAF_Lite will follow before 1.0.

In PEAR status of this package is: %{_status}.

%description -l pl
XML_FOAF pozwala zaawansowanym u¿ytkownikom tworzyæ zaawansowane pliki
FOAF. Projekt FOAF znajduje siê pod adresem
http://www.foaf-project.org/. XML_FOAF_Parser i XML_FOAF_Lite uka¿±
siê przed 1.0.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
