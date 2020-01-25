#
# Conditional build:
%bcond_without	tests	# perform "make test"
#
Summary:	Convert raw text to something with a little HTML formatting
Summary(pl.UTF-8):	Konwersja czystego tekstu na HTML, rozpoznając trochę sformatowania
Name:		txt2html
Version:	2.51
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/txt2html/%{name}-%{version}.tar.gz
# Source0-md5:	e870c5443893b84894aa44980a35b2ea
URL:		http://txt2html.sourceforge.net/
BuildRequires:	perl-Module-Build >= 0.26
%if %{with tests}
BuildRequires:	perl-Getopt-ArgvFile
BuildRequires:	perl-Test-Distribution
BuildRequires:	perl-YAML-Syck
%endif
Requires:	perl-Getopt-ArgvFile
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
My intent in writing this tool is to provide an easier way of
converting existing text documents to HTML format. txt2html can also
be used to aid in writing new HTML documents, but there are probably
better ways of doing that.

%description -l pl.UTF-8
Narzędzie ułatwia konwersję dokumentów tekstowych na HTML. txt2html
może też być użyty do pisania nowych dokumentów HTML, chociaż na to
pewnie istnieją lepsze sposoby.

%prep
%setup -q

%build
%{__perl} Build.PL \
	installdirs=vendor

./Build
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes DEVNOTES TODO
%attr(755,root,root) %{_bindir}/txt2html
%{_mandir}/man*/*
%{perl_vendorlib}/HTML/*.pm
