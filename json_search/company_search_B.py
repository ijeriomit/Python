import json
import re

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
    # Parse the context JSON
    context_data = json.loads(context)
    company = context_data["company"]
    
    # Try to extract a product name from the user input
    product = extract_product(user_input, company)
    
    if product:
        # If a product is found, generate the ICP
        icp = generate_icp(context_data, product)
        
        # Construct the output JSON
        output = {
            "company": context_data["company"],
            "country_iso": context_data["country_iso"],
            "website": context_data["website"],
            "product": product,
            "icp": icp
        }
        return json.dumps(output)
    else:
        # If no product is found, return the error JSON
        return json.dumps({"statusCode": 404, "error": "Product not found"})

def extract_product(user_input, company):
    """Extracts a potential product name from the user input."""
    # Remove the company name from the input
    product = user_input.replace(company, "").strip()
    
    # If there's anything left, consider it a product name
    if product:
        return product
    return None

def generate_icp(context, product):
    """Generates an Ideal Customer Profile based on the company and product."""
    company = context["company"]
    country = context["country_iso"]
    
    # Define some basic ICP templates
    icp_templates = [
        "Our ICP is young adults aged {age_range}, living in {location} areas of {country}, who are interested in {interest}. They are likely to be influenced by {influence} and value {value}.",
        "The ideal customer for {product} is typically {age_range} years old, residing in {location} regions of {country}. They tend to be {characteristic} and prioritize {priority} in their purchasing decisions.",
        "Our target demographic for {product} is {age_range}-year-olds in {country}, particularly those in {location} settings. They are often {trait} consumers who appreciate {appreciation} and are drawn to {attraction}."
    ]
    
    # Choose a random template
    import random
    template = random.choice(icp_templates)
    
    # Fill in the template with appropriate details
    icp = template.format(
        age_range=random.choice(["18-25", "25-35", "35-50", "50-65"]),
        location=random.choice(["urban", "suburban", "rural"]),
        country=country,
        interest=random.choice(["trying new products", "health and wellness", "convenience", "luxury experiences"]),
        influence=random.choice(["social media", "peer recommendations", "traditional advertising", "online reviews"]),
        value=random.choice(["quality", "innovation", "sustainability", "brand reputation"]),
        product=product,
        characteristic=random.choice(["health-conscious", "tech-savvy", "environmentally aware", "budget-minded"]),
        priority=random.choice(["quality", "convenience", "eco-friendliness", "value for money"]),
        trait=random.choice(["discerning", "trendsetting", "practical", "adventurous"]),
        appreciation=random.choice(["premium quality", "innovative features", "ethical production", "personalized experiences"]),
        attraction=random.choice(["cutting-edge technology", "sustainable practices", "exclusive offerings", "lifestyle enhancement"])
    )
    
    return icp

# Example usage:
context = '{"company":"Heineken","country_iso":"ES","website":"https://heineken.com/es"}'
user_input = "Heineken 00"
result = process_user_input(context, user_input)
print(result)
                  