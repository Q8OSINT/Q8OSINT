from phpserialize import serialize, unserialize

def getTokens():
  f = open("./assets/tokens.txt", "rt")
  fstr = f.read()

  pair_tokens = fstr.split("a:4")
  pair_tokens.pop(0)

  tokens = []

  for p_token in pair_tokens:
    p_token = p_token.split("oauth_token")
    p_token = p_token[1].split(":")
    p_token = p_token[2].split('"')
    tokens.append(p_token[1])

  i = 0
  tokens_list = ""
  for token in tokens:
    tokens_list += "<option value'"+token+"'>"+token+"</option>"
  return tokens_list