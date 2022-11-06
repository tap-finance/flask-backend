LensAPIURL = "https://api.lens.dev/playgroun"

LensProfileDataQuery = """query ProfileData($address: EthereumAddress = "0x0000000000000000000000000000000000000001"){
  profiles(request: {
    ownedBy: [$address]
  }){
    items{
      name
      bio
      handle
      picture{
        ... on NftImage{
          contractAddress
          tokenId
          chainId
          uri
        }
      	... on MediaSet{
        	original{
            url
          }
      	}
      }
      isDefault
    }
  }
}"""
