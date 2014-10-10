%define upstream_name    PPI-Tester
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A wxPerl-based interactive PPI debugger/tester
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PPI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::Dumpvar)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Script)
BuildRequires:	perl(Wx)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# require GTK display
# make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{perl_vendorlib}/*
%{_bindir}/ppitester
%{_mandir}/man1/*
%{_mandir}/man3/*


%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-2mdv2011.0
+ Revision: 551995
- rebuild

* Thu Jun 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 389136
- import perl-PPI-Tester


* Thu Jun 25 2009 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist

