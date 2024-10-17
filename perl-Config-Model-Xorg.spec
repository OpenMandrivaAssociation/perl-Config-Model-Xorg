%define upstream_name    Config-Model-Xorg
%define upstream_version 1.104

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Xorg configuration model for Config::Model 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config::Model::CursesUI)
BuildRequires: perl(Config::Model)
BuildRequires: perl(Module::Build)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module provides a configuration model for Xorg.

With this module and Config::Model, you have a tool to tune the configuration of your favourite X server.

Installing Config::Model::CursesUI is recommended as you'll have a more user friendly curses based user interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
#%{_mandir}/man1/*
%{_mandir}/man3/*
#%{_bindir}/config-edit-xorg
%{perl_vendorlib}/Config/Model/Xorg.pm
%{perl_vendorlib}/Config/Model/models/Xorg.pl
%{perl_vendorlib}/Config/Model/models/Xorg/*
