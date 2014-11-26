#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Template
%define		pnam	Plugin-Number-Format
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin/filter interface to Number::Format
Summary(pl.UTF-8):	Wtyczka - interfejs filtru do Number::Format
Name:		perl-Template-Plugin-Number-Format
Version:	1.02
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DARREN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6ccfbc9db84fc86ae64aae9973f037cf
URL:		http://search.cpan.org/dist/Template-Plugin-Number-Format/
BuildRequires:	perl-Number-Format
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin/filter interface to Number::Format.

%description -l pl.UTF-8
Wtyczka - interfejs filtru do Number::Format.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Template/Plugin/Number
%{perl_vendorlib}/Template/Plugin/Number/Format.pm
%{_mandir}/man3/*
