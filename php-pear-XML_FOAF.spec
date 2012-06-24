%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       FOAF
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Provides the ability to manipulate FOAF RDF/XML
Summary(pl):	%{_pearname} - przetwarzanie plik�w FOAF RDF/XML
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0e2bf074ffa2feba8b9e050881db0150
URL:		http://pear.php.net/package/XML_FOAF/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_FOAF allows advanced users to create advanced FOAF files.
The FOAF Project can be found at http://www.foaf-project.org/ -
XML_FOAF_Parser and XML_FOAF_Lite will follow before 1.0.

This class has in PEAR status: %{_status}.

%description -l pl
XML_FOAF pozwala zaawansowanym u�ytkownikom tworzy� zaawansowane pliki
FOAF. Projekt FOAF znajduje si� pod adresem
http://www.foaf-project.org/. XML_FOAF_Parser i XML_FOAF_Lite uka��
si� przed 1.0.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
