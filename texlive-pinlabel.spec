Name:		texlive-pinlabel
Version:	24769
Release:	2
Summary:	A TeX labelling package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pinlabel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pinlabel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pinlabel.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
