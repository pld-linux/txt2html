Summary:	Convert raw text to something with a little HTML formatting
Summary(pl):	Konwersja czystego tekstu na HTML, rozpoznaj±c trochê sformatowania
Name:		txt2html
Version:	1.28
Release:	2
Copyright:	Modified BSD
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Source0:	http://www.aigeek.com/txt2html/%{name}-%{version}.tar.gz
URL:		http://www.aigeek.com/txt2html/
Requires:	perl
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/misc}

sed -e's#%{_prefix}/local/lib#%{_datadir}/misc#' txt2html.pl > \
	$RPM_BUILD_ROOT%{_bindir}/txt2html

install txt2html.dict $RPM_BUILD_ROOT%{_datadir}/misc/txt2html-linkdict

gzip -9nf changes.html sample.txt sample.html LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config %{_datadir}/misc/txt2html-linkdict
%attr(755,root,root) %{_bindir}/txt2html
