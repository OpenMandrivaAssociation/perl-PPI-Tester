%define upstream_name    PPI-Tester
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    A wxPerl-based interactive PPI debugger/tester
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PPI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Devel::Dumpvar)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(PPI)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Script)
BuildRequires: perl(Wx)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This package implements a wxWindows desktop application which provides the
ability to interactively test the PPI perl parser.

The 'PPI::Tester' module implements the application, but is itself of no
use to the user. The launcher for the application 'ppitester' is installed
with this module, and can be launched by simply typing the following from
the command line.

  ppitester

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/ppitester
/usr/share/man/man1/ppitester.1.lzma

