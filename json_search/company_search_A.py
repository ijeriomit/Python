def process_user_input(context, user_input):
  """Processes user input related to a company and potentially identifies a product or service.

  Leverages contextual information about the company to provide insights into the product and its Ideal Customer Profile (ICP).

  Args:
    context: A JSON object containing information about the company.
    user_input: A string representing the user's query.

  Returns:
    A JSON object containing the company information, extracted product name, and ICP if a product is identified.
    If no product is found, returns a JSON object with an error message.
  """
  company_name = context["company"]
  
  # Simple approach: assume anything after the company name is a potential product
  if company_name in user_input:
    potential_product = user_input.replace(company_name, "").strip()
    if not potential_product:
        return {"statusCode":404,"error":"Product not found"}
    
    # Craft an ICP based on company and potential product
    icp = generate_icp(context, potential_product)

    return {
        "company": company_name,
        "country_iso": context["country_iso"],
        "website": context["website"],
        "product": potential_product,
        "icp": icp
    }
  else:
    return {"statusCode":404,"error":"Product not found"}


def generate_icp(context, potential_product):
  """Generates a plausible ICP description based on the company and potential product."""

  company_name = context["company"]
  country = context["country_iso"]

  # Placeholder ICPs based on company type (you can expand this)
  if "Beer" in company_name or "Heineken" in company_name:
    return f"Our ICP is young adults aged 21-35, living in urban areas of {country}, who are interested in trying new beers and enjoy socializing with friends. They are likely to be influenced by social media and advertising campaigns."
  else: 
    # Generic ICP if company type is unknown
    return f"Our ICP is adults aged 25-55, living in {country}, with an interest in {potential_product}. They are likely to be influenced by online reviews and recommendations from friends."

# Example usage:
context = {"company":"Heineken","country_iso":"ES","website":"https://heineken.com/es"}
user_input = "Heineken 00"
result = process_user_input(context, user_input)
print(result)