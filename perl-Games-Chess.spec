%include	/usr/lib/rpm/macros.perl
Summary:	Games-Chess perl module
Summary(pl):	Modu³ perla Games-Chess
Name:		perl-Games-Chess
Version:	0.003
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Games/Games-Chess-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games-Chess provides Games::Chess::Piece and Games::Chess::Position
classes to represent a chess game data.

%description -l pl
Games-Chess udosêpnia klasy Games::Chess::Piece i
Games::Chess::Position s³u¿±ce do przedstawiania danych w grze
szachowej.

%prep
%setup -q -n Games-Chess-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Games/Chess.pm
%{_mandir}/man3/*
