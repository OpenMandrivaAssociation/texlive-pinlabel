%global tl_name pinlabel
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A TeX labelling package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pinlabel
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pinlabel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pinlabel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pinlabel is a labelling package for attaching perfectly formatted TeX
labels to figures and diagrams in both eps and pdf formats. It is
suitable both for labelling a new diagram and for relabelling an
existing diagram. The package uses coordinates derived from GhostView
(or gv) and labels are placed with automatic and consistent spacing
relative to the object labelled.

