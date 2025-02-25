import dns.resolver

def resolve_dns(domain, record_type='A'):
    try:
        # Perform dns resolution
        answers = dns.resolver.resolve(domain, record_type)
        # extract records
        records = []
        for r in answers:
            r = str(r)
            records.append(r)
        ttl = answers.rrset.ttl

        return {
            'domain': domain,
            'type': record_type,
            'records': records,
            'ttl': ttl,
        }
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"domain {domain} does not exist")
    except dns.resolver.NoAnswer:
        raise ValueError(f"No {record_type} records exists for '{domain}'")
    except dns.resolver.Timeout:
        raise ValueError("DNS query timed out")

print(resolve_dns('google.com','A'))

