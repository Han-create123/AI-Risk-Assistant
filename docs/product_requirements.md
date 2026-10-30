# Product Requirements Document: AI Risk Assistant

## 1. Product Problem

Public financial filings, corporate disclosures, and news reports are often lengthy and difficult for entry-level research analysts to review efficiently. Identifying material signals related to leverage, liquidity, profitability, or compliance requires time and judgment. Manual searching can be slow and may lead to important signals being overlooked, resulting in incomplete research and underestimated risk.

AI Risk Assistant addresses this first-screening problem by identifying predefined risk signals in pasted English financial text, providing a short explanation for each signal, and showing the source sentence as evidence. The MVP is a research-support tool only. It does not provide investment advice, client-specific recommendations, credit decisions, or guaranteed risk predictions.

## 2. Target User

The primary users are entry-level equity research analysts with approximately 0–2 years of experience. Secondary users include finance graduate students who want to practice financial-text risk analysis.

Users may review English annual reports, corporate disclosures, and public news. They need a fast way to identify risk signals worth verifying as part of follow-up research, rather than receive final buy/sell conclusions. The web interface should be usable without Python, AI, or advanced data-tool knowledge. The MVP is not limited to a specific market or region.

## 3. MVP Goal

The MVP enables users to paste Chinese or English financial text into a web page and receive a risk-screening result within a few seconds. The result identifies predefined risk categories, provides a short explanation for each signal, highlights the supporting evidence sentence in the pasted source text, and presents a demonstration risk level based on the detected signals.

The first version can be used without registration, login, or API configuration. It is designed for fast research support rather than final investment or credit decisions. Highlighting evidence on original PDF annual-report pages is a future enhancement.

## 4. MVP Scope

The MVP accepts user-pasted Chinese or English financial text. It identifies four predefined categories of risk signals: leverage and repayment risk, liquidity and cash-flow risk, profitability deterioration, and compliance or operational-event risk.

The web interface highlights supporting evidence sentences in the pasted text and presents a result list containing the risk category, a short explanation, and the evidence sentence. It also produces a transparent demonstration risk score from 1 to 5 based on detected signals, where 1 represents Low risk and 5 represents High risk. This score is not a professional credit rating or investment rating.

Users can download the result of an analysis without registration, login, or API configuration. PDF upload and browser-local analysis history are Phase 2 features. Web-link crawling, user accounts, and cloud-saved history are future enhancements.

## 5. User Flow

1. The user opens the web page without registration or login.
2. The user pastes Chinese or English financial text into a large input area, or selects a sample text for demonstration.
3. The user clicks `Analyze Risk`.
4. The result appears on the same page in a two-column layout.
5. The left panel shows the 1–5 demonstration risk score first, followed by the detected risk signals and short explanations.
6. The right panel shows the original source text with evidence sentences highlighted.
7. The user can download an analysis report containing the original text, risk score, detected signals, explanations, and evidence sentences.
8. The user can clear the current text and results, then begin a new analysis.

## 6. Out of Scope and Safety Boundaries

- This tool does not provide investment advice, client-specific recommendations, or buy/sell recommendations.
- Users must review the original text and highlighted evidence. The output is intended to save time during initial research screening, not replace professional judgment.
- The MVP is intended for public or non-confidential text only. Users should not submit unpublished materials, personal data, or sensitive client information.
- The 1–5 risk score is a demonstration screening score. It must not be used alone for real credit decisions, professional credit ratings, or automated financial decisions.
- The system may miss risk signals, misinterpret context, or be unable to calculate professional financial metrics.
- Accuracy must be evaluated with future test cases. Each detected signal should include evidence text to support human review.
- The tool does not verify whether the input text is authentic, current, complete, or from an official source. Users remain responsible for confirming the source and date of the underlying information.

## 7. Success Criteria

The project will be considered successful when:

- A public deployment URL is available and a first-time user can complete an analysis without installing Python or using VS Code.
- Users can paste Chinese or English text and complete an analysis without writing code.
- The web interface reliably displays a 1–5 risk score, detected risk signals, short explanations, and highlighted source evidence.
- Users can download an analysis report.
- The GitHub repository includes runnable code, an English README, this PRD, and demonstration screenshots.
- At least six manually reviewed Chinese and English sample cases are used to check that detected signals and evidence sentences are consistent with the source text.
- The project can be demonstrated end to end: input text, analyze risk, review highlighted evidence, and download a report.