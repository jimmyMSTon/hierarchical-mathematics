# 从证明的生产到知识的吸收

## 面向人工智能时代的分层证明与累积验证范式

**赖俊铭（Chunming LAI）** · 独立研究者
[ORCID: 0009-0002-7594-4535](https://orcid.org/0009-0002-7594-4535) · [联系邮箱](mailto:jimmybus0610@outlook.com) · [English](README.md)

人工智能正在改变数学证明的稀缺性。当机器能够生成超出个体阅读能力的证明时，数学共同体面临的关键问题不仅是获得正确结果，还包括理解、验证、吸收、共享与复用数学知识。

## 阅读论文

| 语言 | 论文 | LaTeX 源码 |
| --- | --- | --- |
| 中文 | [PDF](paper/Paradigm_ZH.pdf) | [源码](source/Paradigm_ZH.tex) |
| English | [PDF](paper/Paradigm_EN.pdf) | [源码](source/Paradigm_EN.tex) |

[技术维护版 v1.0.1](https://github.com/jimmyMSTon/hierarchical-mathematics/releases/tag/v1.0.1) · [原始公开版 v1.0.0](https://github.com/jimmyMSTon/hierarchical-mathematics/releases/tag/v1.0.0)

## 核心框架

相对于既有公共定理库，将目标定理及新证明组织为有限有向无环依赖图。设 $D(v)$ 为新结点 $v$ 的直接新依赖集合。

$$
\ell(v)=\begin{cases}
0,& D(v)=\varnothing,\\
1+\max_{u\in D(v)}\ell(u),& D(v)\ne\varnothing.
\end{cases}
$$

目标定理的层级为 $r=\ell(\mathrm{thm})$。允许不等深分支、跨层引用与共享引理。研究者自底向上理解和验证局部证明，将已经建立的成果纳入公共定理库，并在上层证明及后续研究中复用。目标是使局部证明易于理解，而非规定任意长度上限。

本文区分形式正确性、语义忠实性与数学理解，并给出框架的逻辑性质。实际研究效率方面的潜在收益仍需实践检验。

## 公开倡议

欢迎数学家、人工智能研究者、学术期刊、科研机构以及形式化数学社区讨论、改进并探索这一研究范式。倡议不是要替代现有数学论文、定理库或证明助手，而是强调数学知识的累积吸收与复用。

[参与公开讨论](https://github.com/jimmyMSTon/hierarchical-mathematics/discussions) · [引用信息](CITATION.cff) · [BibTeX](CITATION.bib) · [编译与校验](BUILD.md) · [开放参考文献入口](REFERENCES.md)

## 发表状态及许可

论文为研究立场与形式框架论文，尚无独立同行评审、DOI 或 arXiv 编号。AI 参与情况见论文内披露。论文日期为 2026 年 11 月 24 日，GitHub 原始公开日期为 2026 年 11 月 25 日。v1.0.1 仅修复中文版 PDF 字符映射和仓库技术文档，未修改论文数学内容。

论文与原创研究文档采用 [CC BY 4.0](LICENSE) 许可。
