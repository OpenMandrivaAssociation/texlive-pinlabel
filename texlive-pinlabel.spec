Name:		texlive-pinlabel
Version:	1.1
Release:	1
Summary:	A TeX labelling package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pinlabel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pinlabel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pinlabel.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Pinlabel is a labelling package for attaching perfectly
formatted TeX labels to figures and diagrams in both eps and
pdf formats. It is suitable both for labelling a new diagram
and for relabelling an existing diagram. The package uses
coordinates derived from GhostView (or gv) and labels are
placed with automatic and consistent spacing relative to the
object labelled.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pinlabel/pinlabel.sty
%doc %{_texmfdistdir}/doc/latex/pinlabel/README
%doc %{_texmfdistdir}/doc/latex/pinlabel/pinlabdoc.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/fig3.eps
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/fig3.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/fig6.eps
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/fig6.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/gtpart.cls
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/pinlabdoc.tex
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put.eps
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put.fig
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put2.eps
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put2.fig
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/put2.pdf
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/screen.eps
%doc %{_texmfdistdir}/doc/latex/pinlabel/src/screen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
