Summary:	Convert raw text to something with a little HTML formatting
Summary(pl):	Konwersja czystego tekstu na HTML, rozpoznaj±c trochê sformatowania
Name:		txt2html
Version:	2.10
Release:	1
License:	BSD-like
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/txt2html/%{name}-%{version}.tar.gz
# Source0-md5:	938aae0d317c5cbd87b077f1696f5a62
URL:		http://www.sourceforge.net/projects/txt2html/
#BuildRequires:	perl-ExtUtils-configPL
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
My intent in writing this tool is to provide an easier way of
converting existing text documents to HTML format. txt2html can also
be used to aid in writing new HTML documents, but there are probably
better ways of doing that.

%description -l pl
Narzêdzie u³atwia konwersjê dokumentów tekstowych na HTML. txt2html
mo¿e te¿ byæ u¿yty do pisania nowych dokumentów HTML, chocia¿ na to
pewnie istniej± lepsze sposoby.

%prep
%setup -q

%build
#sed -e's#%{_prefix}/local/lib#%{_datadir}/misc#' txt2html.pl > \
#	txt2html
perl Makefile.PL
%{__make}
%{__make} test
#%{__make} install

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/misc}

install txt2html $RPM_BUILD_ROOT%{_bindir}
install txt2html.dict $RPM_BUILD_ROOT%{_datadir}/misc/txt2html-linkdict

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README Changes DEVNOTES README TODO
%config %{_datadir}/misc/txt2html-linkdict
%attr(755,root,root) %{_bindir}/txt2html
