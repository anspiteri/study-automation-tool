"""
The "llm" package provides the logic required for interfacing with the APIs of the various large lanugage models.

This was designed with the "strategy" design pattern in mind, whereby a base "llm_client" is provided,
with concrete llm_clients containing the specific code used for their vendor api's. These can be
added to, and updated as required.
"""
