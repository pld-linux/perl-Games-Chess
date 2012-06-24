%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	Chess
Summary:	Games::Chess Perl module
Summary(cs):	Modul Games::Chess pro Perl
Summary(da):	Perlmodul Games::Chess
Summary(de):	Games::Chess Perl Modul
Summary(es):	M�dulo de Perl Games::Chess
Summary(fr):	Module Perl Games::Chess
Summary(it):	Modulo di Perl Games::Chess
Summary(ja):	Games::Chess Perl �⥸�塼��
Summary(ko):	Games::Chess �� ����
Summary(nb):	Perlmodul Games::Chess
Summary(pl):	Modu� Perla Games::Chess
Summary(pt):	M�dulo de Perl Games::Chess
Summary(pt_BR):	M�dulo Perl Games::Chess
Summary(ru):	������ ��� Perl Games::Chess
Summary(sv):	Games::Chess Perlmodul
Summary(uk):	������ ��� Perl Games::Chess
Summary(zh_CN):	Games::Chess Perl ģ��
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
Games::Chess provides Games::Chess::Piece and Games::Chess::Position
classes to represent a chess game data.

%description -l pl
Games::Chess udost�pnia klasy Games::Chess::Piece i
Games::Chess::Position s�u��ce do przedstawiania danych w grze
szachowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Games/Chess.pm
%{_mandir}/man3/*
