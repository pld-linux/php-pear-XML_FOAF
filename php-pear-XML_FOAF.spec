%define		status		beta
%define		pearname	XML_FOAF
Summary:	%{pearname} - provides the ability to manipulate FOAF RDF/XML
Summary(pl.UTF-8):	%{pearname} - przetwarzanie plików FOAF RDF/XML
Name:		php-pear-%{pearname}
Version:	0.4.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	204f435c64ad5704451e156a403335e4
URL:		http://pear.php.net/package/XML_FOAF/
BuildRequires:	php-pear-PEAR >= 1:1.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 4.3.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.0-0.b1
Requires:	php-pear-RDF >= 0.1.0-0.alpha1
Requires:	php-pear-XML_Beautifier >= 0.2.2
Requires:	php-pear-XML_Tree >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_FOAF allows advanced users to create advanced FOAF files. The FOAF
Project can be found at <http://www.foaf-project.org/> -
XML_FOAF_Parser and XML_FOAF_Lite will follow before 1.0.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
XML_FOAF pozwala zaawansowanym użytkownikom tworzyć zaawansowane pliki
FOAF. Projekt FOAF znajduje się pod adresem
<http://www.foaf-project.org/>. XML_FOAF_Parser i XML_FOAF_Lite ukażą
się przed 1.0.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
mv docs/%{pearname}/docs/examples .
mv .%{php_pear_dir}/data/XML_FOAF/README .

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
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/FOAF
%{_examplesdir}/%{name}-%{version}
