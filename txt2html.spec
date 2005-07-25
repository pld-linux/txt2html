#
# Conditional build:
%bcond_without	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Convert raw text to something with a little HTML formatting
Summary(pl):	Konwersja czystego tekstu na HTML, rozpoznaj�c troch� sformatowania
Name:		txt2html
Version:	2.41
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/txt2html/%{name}-%{version}.tar.gz
# Source0-md5:	fe6f80191860e2724e113a643a9da62a
URL:		http://txt2html.sourceforge.net/
BuildRequires:	perl-Module-Build >= 0.26
Requires:	perl-Getopt-ArgvFile
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
My intent in writing this tool is to provide an easier way of
converting existing text documents to HTML format. txt2html can also
be used to aid in writing new HTML documents, but there are probably
better ways of doing that.

%description -l pl
Narz�dzie u�atwia konwersj� dokument�w tekstowych na HTML. txt2html
mo�e te� by� u�yty do pisania nowych dokument�w HTML, chocia� na to
pewnie istniej� lepsze sposoby.

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
