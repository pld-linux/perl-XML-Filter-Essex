#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Filter-Essex
Summary:	XML::Handler::Essex - Essex handler object (including XML::Filter::Essex)
Summary(pl):	XML::Handler::Essex - obiekt uchwytu Essex (obejmuj±cy XML::Filter::Essex)
Name:		perl-XML-Filter-Essex
Version:	0.01
Release:	1
# any version of these, same as perl for XML::SAX::Writer::XML
License:	BSD or Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	96543bde209be70cc2b0a398680cc7e7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IPC-Run
BuildRequires:	perl-XML-Filter-Dispatcher >= 0.4
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Writer >= 0.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Defines (and exports, by default) get() and get_...() routines that
allow an Essex handler and filter to pull events from the SAX stream.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/Essex
%{perl_vendorlib}/%{pdir}/Filter/*
%{perl_vendorlib}/%{pdir}/Generator/*
%{perl_vendorlib}/%{pdir}/Handler/*
%{perl_vendorlib}/%{pdir}/SAX/Writer/*.pm
%{_mandir}/man3/*
