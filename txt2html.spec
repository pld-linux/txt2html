Summary:     Convert raw text to something with a little HTML formatting
Summary(pl): Konwersja czystego tekstu na HTML, rozpoznaj±c trochê sformatowania
Name:        txt2html
Version:     1.25
Release:     3
Copyright:   Modified BSD
Group:       Utilities/Text
Source:      http://www.thehouse.org/txt2html/%{name}-%{version}.tar.gz
URL:         http://www.thehouse.org/txt2html/
Requires:    perl
BuildRoot:   /tmp/%{name}-%{version}-root
BuildArchitectures: noarch

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
install -d $RPM_BUILD_ROOT/usr/{bin,lib}
{
    echo '#!/usr/bin/perl'
    sed -e'1,10d' -e's%/usr/local/lib%/usr/lib%' txt2html.pl
} >$RPM_BUILD_ROOT/usr/bin/txt2html
install txt2html.dict $RPM_BUILD_ROOT/usr/lib/txt2html-linkdict

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc changes.html sample.txt sample.html LICENSE README
%config /usr/lib/txt2html-linkdict
%attr(755, root, root) /usr/bin/txt2html

%changelog
* Fri Sep 25 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
  [1.25-3]
- added pl translation,
- added %setup -q parameter,
- replaced `mkdir -p' with more standard `install -d',
- minor clean-ups in the install script.
