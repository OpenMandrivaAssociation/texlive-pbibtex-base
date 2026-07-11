%global tl_name pbibtex-base
%global tl_revision 66085

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bibliography styles and miscellaneous files for pBibTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/pbibtex/pbibtex-base
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbibtex-base.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbibtex-base.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These are miscellaneous files, including bibliography styles (.bst), for
pBibTeX, which is a Japanese extended version of BibTeX contained in TeX
Live. The bundle is a redistribution derived from the ptex-texmf
distribution by ASCII MEDIA WORKS.

