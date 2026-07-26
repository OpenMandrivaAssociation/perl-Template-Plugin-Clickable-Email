%define upstream_name    Template-Plugin-Clickable-Email
Name:       perl-%{upstream_name}
Version:    0.01
Release:    5

Summary:    Make email addresses in to HTML links
License:    Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/Template-Plugin-Clickable-Email
Source0:    https://cpan.metacpan.org/authors/id/N/NI/NIKC/Template-Plugin-Clickable-Email-%{version}.tar.gz

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
%setup -q -n %{upstream_name}-%{version}

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


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 405533
- rebuild using %0.01 Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-4mdv2009.0
+ Revision: 258463
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-3mdv2009.0
+ Revision: 246504
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.01-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2007.1
+ Revision: 138868
- Imported perl-Template-Plugin-Clickable-Email-0.01-1mdv2007.1 into SVN repository.

* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2007.1
- first mdv release

