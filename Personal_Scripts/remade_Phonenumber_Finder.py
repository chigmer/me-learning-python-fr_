import re
pattern = re.compile(r"""

(?: \(?\d{3}\)?)?
(?:\s|-|\.)? #ensure that the separator is optional incase area code is missing
\d{3}
(?:\s|-|\.)
\d{4}

#ensured no capturing groups to ruin findall()
""", re.VERBOSE)


print(pattern.findall("\"Yesterday, I called my friend at 415-555-1234 to confirm our plans, but she asked me to try her office instead at (212) 444-5678. Later, I needed tech support, so I dialed 800.123.4567 and got a helpful agent. My cousin lives in another state, so I texted him at 303 987 6543. A local vendor shared their contact: (619)777-8901, and another vendor gave 510-555-6789. For emergencies, there’s a hotline 911-0000. Finally, our family reunion organizer can be reached at 707.333.4444 and her assistant at (408)-222-1111.\"")) #from AI