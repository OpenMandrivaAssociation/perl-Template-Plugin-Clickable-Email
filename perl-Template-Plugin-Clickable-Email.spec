%define upstream_name    Template-Plugin-Clickable-Email
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Make email addresses in to HTML links
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:  perl(Module::Build)
Buildrequires:  perl(Template)
Buildrequires:  perl(Email::Find)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Template::Plugin::Clickable::Email converts any e-mail addresses found in the
filtered text in to HTML mailto: links.

This module uses Email::Find, see the documentation for that module for caveats
relating to how addresses are parsed, and why some false positives may occur.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
