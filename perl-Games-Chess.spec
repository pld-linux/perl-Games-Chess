#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	Chess
Summary:	Games::Chess - represent chess positions and games
Summary(pl):	Games::Chess - reprezentacja ruchów i pozycji szachowych
Name:		perl-Games-Chess
Version:	0.003
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	42f05fe388999fd712e3011b9f39bd70
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games::Chess Perl module provides Games::Chess::Piece and
Games::Chess::Position classes to represent a chess game data.

%description -l pl
Modu³ Perla Games::Chess udostêpnia klasy Games::Chess::Piece i
Games::Chess::Position s³u¿±ce do przedstawiania danych w grze
szachowej.

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
%doc README
%{perl_vendorlib}/Games/Chess.pm
%{_mandir}/man3/*
