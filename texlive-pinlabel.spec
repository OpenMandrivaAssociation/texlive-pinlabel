# revision 24769
# category Package
# catalog-ctan /macros/latex/contrib/pinlabel
# catalog-date 2011-12-05 18:34:00 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-pinlabel
Version:	1.2
Release:	12
Summary:	A TeX labelling package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pinlabel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pinlabel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pinlabel.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pinlabel is a labelling package for attaching perfectly
formatted TeX labels to figures and diagrams in both eps and
pdf formats. It is suitable both for labelling a new diagram
and for relabelling an existing diagram. The package uses
coordinates derived from GhostView (or gv) and labels are
placed with automatic and consistent spacing relative to the
object labelled.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pinlabel/pinlabel.sty
%doc %{_texmfdistdir}/doc/latex/pinlabel/pinlabdoc.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/fig3.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/fig6.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/gtpart.cls
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/pinlabdoc.tex
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put.fig
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put2.fig
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put2.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/screen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 754906
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 739868
- texlive-pinlabel

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719262
- texlive-pinlabel
- texlive-pinlabel
- texlive-pinlabel
- texlive-pinlabel

