Name:		texlive-ieeepes
Version:	4.0
Release:	1
Summary:	IEEE Power Engineering Society Transactions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ieeepes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeepes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeepes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Supports typesetting of transactions, as well as discussions
and closures, for the IEEE Power Engineering Society
Transactions journals.

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
%{_texmfdistdir}/bibtex/bst/ieeepes/ieeepes.bst
%{_texmfdistdir}/tex/latex/ieeepes/ieeepes.sty
%doc %{_texmfdistdir}/doc/latex/ieeepes/README
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_check.bib
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_check.tex
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_doc.pdf
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_doc.tex
%doc %{_texmfdistdir}/doc/latex/ieeepes/ieeepes_skel.tex
%doc %{_texmfdistdir}/doc/latex/ieeepes/vk.eps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
