%include	/usr/lib/rpm/macros.perl
%define	pdir	Games
%define	pnam	Chess
Summary:	Games::Chess perl module
Summary(pl):	Modu³ perla Games::Chess
Name:		perl-Games-Chess
Version:	0.003
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games::Chess provides Games::Chess::Piece and Games::Chess::Position
classes to represent a chess game data.

%description -l pl
Games::Chess udostêpnia klasy Games::Chess::Piece i
Games::Chess::Position s³u¿±ce do przedstawiania danych w grze
szachowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Games/Chess.pm
%{_mandir}/man3/*
