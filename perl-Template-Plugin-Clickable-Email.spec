%define module  Template-Plugin-Clickable-Email
%define name    perl-%{module}
%define version 0.01
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Make email addresses in to HTML links
License:        Artistic
group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Template/%{module}-%{version}.tar.bz2
Buildrequires:  perl(Module::Build)
Buildrequires:  perl(Template)
Buildrequires:  perl(Email::Find)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}

%description
Template::Plugin::Clickable::Email converts any e-mail addresses found in the
filtered text in to HTML mailto: links.

This module uses Email::Find, see the documentation for that module for caveats
relating to how addresses are parsed, and why some false positives may occur.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Template
%{_mandir}/*/*


