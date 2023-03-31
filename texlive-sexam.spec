Name:		texlive-sexam
Version:	46628
Release:	2
Summary:	Package for typesetting arabic exam scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sexam
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sexam.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sexam.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a modified version of the exam package
made compatible with XeLaTeX/polyglossia to typesetting arabic
exams.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/sexam
%doc %{_texmfdistdir}/doc/xelatex/sexam

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
