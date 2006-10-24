#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Template
%define		pnam	Plugin-Number-Format
Summary:	Plugin/filter interface to Number::Format
Summary(pl):	Wtyczka - interfejs filtru do Number::Format
Name:		perl-Template-Plugin-Number-Format
Version:	1.01
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0822bca562c536abc3450cebd66c83f1
BuildRequires:	perl-Number-Format
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin/filter interface to Number::Format.

%description -l pl
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
