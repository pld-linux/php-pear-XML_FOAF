%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	FOAF
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides the ability to manipulate FOAF RDF/XML
Summary(pl):	%{_pearname} - przetwarzanie plików FOAF RDF/XML
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fc90f044ef01832ab9c4999b1325bd71
URL:		http://pear.php.net/package/XML_FOAF/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/FOAF/RAP/{model,rdql,syntax,util,vocabulary}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/RAP/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/RAP
install %{_pearname}-%{version}/%{_subclass}/RAP/model/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/RAP/model
install %{_pearname}-%{version}/%{_subclass}/RAP/rdql/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/RAP/rdql
install %{_pearname}-%{version}/%{_subclass}/RAP/syntax/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/RAP/syntax
install %{_pearname}-%{version}/%{_subclass}/RAP/util/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/RAP/util
install %{_pearname}-%{version}/%{_subclass}/RAP/vocabulary/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/RAP/vocabulary

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
