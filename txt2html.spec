Summary:	Convert raw text to something with a little HTML formatting
Summary(pl):	Konwersja czystego tekstu na HTML, rozpoznaj±c trochê sformatowania
Name:		txt2html
Version:	1.25
Release:	4
Copyright:	Modified BSD
Group:		Utilities/Text
Source:		http://www.thehouse.org/txt2html/%{name}-%{version}.tar.gz
URL:		http://www.thehouse.org/txt2html/
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch

%description
My intent in writing this tool is to provide an easier way of converting
existing text documents to HTML format. txt2html can also be used to aid in
writing new HTML documents, but there are probably better ways of doing
that.

%description -l pl
Narzêdzie u³atwia konwersjê dokumentów tekstowych na HTML. txt2html mo¿e te¿
byæ u¿yty do pisania nowych dokumentów HTML, chocia¿ na to pewnie istniej±
lepsze sposoby.

%prep
%setup -n txt2html -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/misc}
{
    echo '#!%{_bindir}/perl'
    sed  -e's#/usr/local/lib#%{_datadir}/misc#' txt2html.pl
} >$RPM_BUILD_ROOT%{_bindir}/txt2html
install txt2html.dict $RPM_BUILD_ROOT%{_datadir}/misc/txt2html-linkdict

gzip -9nf changes.html sample.txt sample.html LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config %{_datadir}/misc/txt2html-linkdict
%attr(755,root,root) %{_bindir}/txt2html

%changelog
* Mon Jul  5 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.25-4]
- more rpm macros,
- txt2html-linkdict moved to %%{_datadir}/misc/ (FHS 2.0),
- gzipping %doc.

* Fri Sep 25 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
  [1.25-3]
- added pl translation,
- added %setup -q parameter,
- replaced `mkdir -p' with more standard `install -d',
- minor clean-ups in the install script.
