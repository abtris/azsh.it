# Mastodon Posts

## 2025-03-10T07:44:25.429Z

Day 411. Even more impressive than the shit from day 13. It now can take [#Azure](https://mastodon.social/tags/Azure) over 10 minutes to delete a custom role definition.

[View post](https://mastodon.social/@azureshit/114137016921286930)

---

## 2025-03-07T08:26:55.108Z

Day 410. [#Microsoft](https://mastodon.social/tags/Microsoft) used to name their sustainability reports after the financial year they have been created for, but suddenly the report for 2023 is called "2024 Environmental Sustainability Report" - which got released mid 2024.

[View post](https://mastodon.social/@azureshit/114120197085490823)

---

## 2025-03-06T08:27:58.538Z

Day 409. Back with yet another installment of: Completely uesless case-sensitive resource ID validation in the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider when all other Azure clients completely ignore it and give you the exact ID the Terraform provider then rejects.

[View post](https://mastodon.social/@azureshit/114114538932316204)

---

## 2025-03-05T07:56:05.584Z

Day 408. Deployment of this [#Azure](https://mastodon.social/tags/Azure) VMSS through [#Terraform](https://mastodon.social/tags/Terraform) failed because Azure does not have sufficient capacity. But the scale set still got created, its instances were just in "Deallocated" state. But since Terraform thinks the deployment failed, if you re-run the Terraform apply, it will fail because the scale set already exists.

[View post](https://mastodon.social/@azureshit/114108751254112060)

---

## 2025-03-04T06:52:27.421Z

Day 407. Because of the shit from day 406 we need to use dedicated mapping tables to run aggregation queries on the exported data from the [#Azure](https://mastodon.social/tags/Azure) Carbon Optimization API and Azure Cost Management API. There does not seem to be a single Azure location that has a consistent name across both APIs.

[View post](https://mastodon.social/@azureshit/114102838715816732)

---

## 2025-03-03T08:53:47.204Z

Day 406. The [#Azure](https://mastodon.social/tags/Azure) Cost Management API and the Azure Carbon Optimization API are using inconsistent names for Azure locations. Because of that you can't easily aggregate their data.

[View post](https://mastodon.social/@azureshit/114097653494588413)

---

## 2025-03-02T16:02:05.789Z

Day 405. When using a Spot node pool in your [#Azure](https://mastodon.social/tags/Azure) Kubernetes Service cluster, the [#Terraform](https://mastodon.social/tags/Terraform) docs tell you that the "eviction\_policy" will default to "Delete", but if you don't explicitly set it in your resource configuration, Terraform will replace your node pool on every apply because it thinks you want "eviction\_policy" to be set to null.

[View post](https://mastodon.social/@azureshit/114093675366571077)

---

## 2025-03-01T10:32:26.768Z

Day 404. Both the [#Azure](https://mastodon.social/tags/Azure) Carbon Optimization API and the [#Microsoft](https://mastodon.social/tags/Microsoft) Cloud for Sustainability API do not provide emissions data for co-located data centers which includes all data centers in Germany.

[View post](https://mastodon.social/@azureshit/114086716817373395)

---

## 2025-02-28T09:28:24.529Z

Day 403. Recently there was a [#Microsoft](https://mastodon.social/tags/Microsoft) Cloud for Sustainability Technical Summit but it feels like it actually was a [#Copilot](https://mastodon.social/tags/Copilot) summit with some sustainability sprinkled on top. (These screenshots are from the first three sessions alone.)

[View post](https://mastodon.social/@azureshit/114080802702955304)

---

## 2025-02-27T08:37:53.057Z

Day 402. These new [#AI](https://mastodon.social/tags/AI) features in the [#Azure](https://mastodon.social/tags/Azure) CLI are working great so far.

[View post](https://mastodon.social/@azureshit/114074941721804051)

---

## 2025-02-26T09:13:01.540Z

Day 401. Just one of the countless instances of links to [#Azure](https://mastodon.social/tags/Azure) docs directing you to sections that don't even exist. via [@joeycdev](https://mastodon.social/@joeycdev)

[View post](https://mastodon.social/@azureshit/114069417592819431)

---

## 2025-02-25T08:33:38.065Z

Day 400. The [#Azure](https://mastodon.social/tags/Azure) Carbon Optimization Dashboard currently only shows corrupted data where all emissions get attributed to "Others" instead of the correct region, except for the most recent month. Attribution to the correct regions used to work a few weeks back but seemingly is broken now.

[View post](https://mastodon.social/@azureshit/114063600389814152)

---

## 2025-02-24T09:17:14.822Z

Day 399. Following up on the shit from day 398, the only way to figure out valid values for request properties of the [#Azure](https://mastodon.social/tags/Azure) Carbon Optimization API is to just try out the API and check out the error messages.

[View post](https://mastodon.social/@azureshit/114058109571428438)

---

## 2025-02-21T11:11:37.639Z

Day 398. When trying to use the [#Azure](https://mastodon.social/tags/Azure) Carbon Optimization API, the docs are pretty much useless and don't tell you what valid values for the request properties are. You only know that they are strings. It's just trial and error.

[View post](https://mastodon.social/@azureshit/114041572401731316)

---

## 2025-02-20T07:00:12.729Z

Day 397. [#Terraform](https://mastodon.social/tags/Terraform) wasn't able to find our [#Azure](https://mastodon.social/tags/Azure) "Public I P address".

[View post](https://mastodon.social/@azureshit/114034921486123874)

---

## 2025-02-19T10:03:23.139Z

Day 396. Our [#Azure](https://mastodon.social/tags/Azure) Function App host apparently died, resulting in timeouts and Internal Server Errors. And there are no logs and no error messages at all. There is no way to figure out what went wrong.

[View post](https://mastodon.social/@azureshit/114029979443839214)

---

## 2025-02-18T07:40:54.606Z

Day 395. We have already had so many issues with the [#Azure](https://mastodon.social/tags/Azure) Firewall, but this might actually be the first time a deployment simply failed with an "Internal Server Error".

[View post](https://mastodon.social/@azureshit/114023756896840206)

---

## 2025-02-17T08:19:30.575Z

Day 394. An [#Azure](https://mastodon.social/tags/Azure) Firewall must be in the same resource group as the vnet you deploy it to - which is a limitation many other Azure services don't have and of course does not get explained.

[View post](https://mastodon.social/@azureshit/114018246365586867)

---

## 2025-02-14T00:57:03.281Z

Day 393. This API endpoint of the [#Azure](https://mastodon.social/tags/Azure) Carbon Optimization API uses a POST request to read the range of available data. But hey, it's a preview version, they will definitely fix that in GA, right? Right??

[View post](https://mastodon.social/@azureshit/113999519630645768)

---

## 2025-02-12T10:13:45.533Z

Day 392. Apparently [#Azure](https://mastodon.social/tags/Azure) considers an Internal Server Error to be your fault now.

[View post](https://mastodon.social/@azureshit/113990384060243725)

---

## 2025-02-11T10:59:43.088Z

Day 391. Recently the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider finally introduced the 'immutability' property for Backup Vaults and because we overlooked this change the new default behavior (which was not flagged as breaking change) promptly led to the recreation of our Backup Vault. Funnily enough this immediately failed because locked Backup Vaults ending up in soft-deleted state cannot get recreated by Terraform, as we covered on day 191.

[View post](https://mastodon.social/@azureshit/113984902468999075)

---

## 2025-02-10T07:34:56.029Z

Day 390. Our [#Azure](https://mastodon.social/tags/Azure) Function App shows us this random error mesage, but clicking on it will simply open a new tab with this error message in the URL bar. Which then doesn't do anything, probably because your browser thinks the "Azure.Identity" part at the beginnging is an URL.

[View post](https://mastodon.social/@azureshit/113978434913772660)

---

## 2025-02-07T09:11:48.911Z

Day 389. When viewing a reservation in the [#Azure](https://mastodon.social/tags/Azure) Portal, instead of using the reservation's display name you get a combination of three UUIDs which is really helpful.

[View post](https://mastodon.social/@azureshit/113961828935243370)

---

## 2025-02-06T09:43:23.158Z

Day 388. Regarding the shit from day 387, as you would expect, the community is not happy with [#Microsoft](https://mastodon.social/tags/Microsoft) shutting down yet another acutally useful tool without having any proper alternative in place.

[View post](https://mastodon.social/@azureshit/113956290766405787)

---

## 2025-02-05T11:43:02.957Z

Day 387. [#Microsoft](https://mastodon.social/tags/Microsoft) is shutting down its public [#Azure](https://mastodon.social/tags/Azure) VM selector tool and recommends you to use [#Copilot](https://mastodon.social/tags/Copilot) in Azure instead. Besides Copilot being a LLM that might help you only somtimes and you totally cannot rely on, with this change you are now required to be signed in to an Azure tenant and have access to an active subscription to be able to get VM recommendations for your theoretical compute workloads.

[View post](https://mastodon.social/@azureshit/113951098991560059)

---

## 2025-02-04T09:30:58.697Z

Day 386. Following up on the shit from day 385, we found two workarounds to figure out the billing subscription of an [#Azure](https://mastodon.social/tags/Azure) reservation:  
1. Check the API requests the Azure Portal makes, the response will contain the "billingScopeId".  
2. In the Portal, go to "Configuration" > "Scope" and switch it to "Single subscription". The subscription that gets populated is your billing subscription.

[View post](https://mastodon.social/@azureshit/113944917357027824)

---

## 2025-02-03T08:45:14.506Z

Day 385. Continuing the shit from day 378, not only can't you see the selected billing subscription during the check out process when buying a reservation in the [#Azure](https://mastodon.social/tags/Azure) Portal, there is also no way to see it when viewing an already purchsed reservation.

[View post](https://mastodon.social/@azureshit/113939075203203673)

---

## 2025-01-31T11:36:26.742Z

Day 384. When creating resource locks for route tables through the [#Azure](https://mastodon.social/tags/Azure) Portal, you can only create them for a whole route table and not scoped to a single route, which is possible when you do it through the API.

[View post](https://mastodon.social/@azureshit/113922761473272350)

---

## 2025-01-30T09:05:21.644Z

Day 383. When viewing the [#Microsoft](https://mastodon.social/tags/Microsoft) Defender for Cloud regulatory compliance in the [#Azure](https://mastodon.social/tags/Azure) Portal there is no intuitive way to select what Azure subscriptions you want to view. You have to select them in "Overview" and that selection then also applies to "Regulatory compliance".

[View post](https://mastodon.social/@azureshit/113916505072561601)

---

## 2025-01-29T08:47:24.212Z

Day 382. When purchasing a reservation through the [#Azure](https://mastodon.social/tags/Azure) Portal, per default the UI will hide the 1 year commitment plans and only show you 3 year commitment plans. We are certain that this is just [#Microsoft](https://mastodon.social/tags/Microsoft) helping you to save more money and not them trying to get you to buy more expensive reservations.

[View post](https://mastodon.social/@azureshit/113910772149545176)

---

## 2025-01-28T09:45:47.445Z

Day 381. Following up on the shit from day 380, [#Microsoft](https://mastodon.social/tags/Microsoft) only recently added a shutdown notice to the [#Azure](https://mastodon.social/tags/Azure) Resource Explorer site, even though the decision to shut it down was made more than six months ago. via [@fowl2](https://hachyderm.io/@fowl2)

[View post](https://mastodon.social/@azureshit/113905339428923445)

---

## 2025-01-27T08:39:50.639Z

Day 380. [#Microsoft](https://mastodon.social/tags/Microsoft) is shutting down the [#Azure](https://mastodon.social/tags/Azure) Resource Explorer (resources.azure.com) which - even though it did not support many newer Azure resources and data models - was one of the few actually helpful tools to debug Azure shit, because it always showed you the actual configuration of resources. You can't say that about the annoying Azure Portal that ignores resources properties and even whole resource types, or about the Azure CLI where every second command is in preview. via [@fowl2](https://hachyderm.io/@fowl2)

[View post](https://mastodon.social/@azureshit/113899417804674486)

---

## 2025-01-24T10:27:14.078Z

Day 379. In case you haven't yet encountered enough arbitrary [#Azure](https://mastodon.social/tags/Azure) limitations: According to the docs, the user data passed to Azure VMs can be at most 64kB. But interestingly the API will tell you it can be at most ~439k chars and we are not sure how you get from the one value to the other one.

[View post](https://mastodon.social/@azureshit/113882853151161627)

---

## 2025-01-22T09:57:03.057Z

Day 378. When buying a reservation through the [#Azure](https://mastodon.social/tags/Azure) Portal, you always need to select a billing subscription the reservation will get billed to, regardless of its scope. But when reviewing during the check out process you have no way to review what billing subscription or even billing account your reservation gets billed to.

[View post](https://mastodon.social/@azureshit/113871409843481970)

---

## 2025-01-21T06:19:23.252Z

Day 377. In [#Azure](https://mastodon.social/tags/Azure), reservations and capacity reservations are two totally different resources which don't have anything in common at all. They even have different resource provider namespaces (you only know that when looking into the data model, of course). But to make it more confusing, the latter ones are sometimes also called "capacity priority reservations" or "on-demand capacity reservations", depending on the documentation you look into.

[View post](https://mastodon.social/@azureshit/113864891645796789)

---

## 2025-01-20T08:48:51.652Z

Day 376. The [#Azure](https://mastodon.social/tags/Azure) Advisor tells us that we can save money by purchasing reservations for our Azure Database for PostgreSQL flexible server, but when we click on the recommended action it tells us the the recommended quantity of reservations is 0.

[View post](https://mastodon.social/@azureshit/113859817088427070)

---

## 2025-01-17T09:03:21.172Z

Day 375. When using the 'az role assignment list' command to list role assignment but you don't have permission to look up information about the assignee you provided, the [#Azure](https://mastodon.social/tags/Azure) CLI will warn you to please supply more specific information about the assignee using '--assignee-object-id' and '--assignee-principal-type'. But if you use them the CLI will tell you that these arguments are not supported.

[View post](https://mastodon.social/@azureshit/113842887138499756)

---

## 2025-01-16T08:52:19.051Z

Day 374. The [#Azure](https://mastodon.social/tags/Azure) Portal is now abusing its notifications panel for advertisements for some [#AI](https://mastodon.social/tags/AI) crap.

[View post](https://mastodon.social/@azureshit/113837181438933121)

---

## 2025-01-15T09:23:36.806Z

Day 373. It takes the [#Azure](https://mastodon.social/tags/Azure) CLI every time almost exactly 30 seconds to show you details of a management group.

[View post](https://mastodon.social/@azureshit/113831642189107572)

---

## 2025-01-14T09:07:17.112Z

Day 372. Back with yet another installment of: Error messages in the [#Azure](https://mastodon.social/tags/Azure) Portal are completely useless and you should always check the response of the API request. This time the Portal tells you to retry cancelling the subscription, even though the API tells you that you will never be able to cancel the subscription because it already has been canceled.

[View post](https://mastodon.social/@azureshit/113825915673473334)

---

## 2025-01-13T08:12:24.832Z

Day 371. When adding DNS configuration to a Private Endpoint using the [#Azure](https://mastodon.social/tags/Azure) CLI, the docs tell you that the "--name" parameter is optional (which doesn't make any sense), but if you omit it the CLI crashes and tells you that the parameter "privateDnsZoneGroupName" is missing, which is probably a response from the API since there is no parameter called like that in the CLI.

[View post](https://mastodon.social/@azureshit/113820037600228698)

---

## 2025-01-10T09:06:52.624Z

Day 370. Continuing the shit from day 369, having a Private Link DNS zone called 'privatelink.westeurope.azurecontainerapps.io' means that you need to create one dedicated zone for each region you want to support. As opposed to having just one 'privatelink.azurecr.io' zone where a configured Private Endpoint could create a DNS record for its specific region in.

[View post](https://mastodon.social/@azureshit/113803264827049406)

---

## 2025-01-09T09:07:28.866Z

Day 369. Some Private Link supported [#Azure](https://mastodon.social/tags/Azure) services have regional Private Link DNS zones, which means for some reason the name of the region the service is located in needs to be in the name of the associated Private Link DNS zone. Usually the region name is in front of the 'privatelink' label, for example 'westeurope.privatelink.azurecr.io', but of course there are some services that do it the other way around, for example 'privatelink.westeurope.azurecontainerapps.io'.

[View post](https://mastodon.social/@azureshit/113797604891049088)

---

## 2025-01-08T07:54:03.890Z

Day 368. We do not understand why the [#Azure](https://mastodon.social/tags/Azure) Portal shows the Traffic Manager DNS name starting with "http://" when it is just a DNS-based load balancer and does not provide any HTTP endpoints to connect to at all. It could be used for all kinds of protocols and this is really confusing.

[View post](https://mastodon.social/@azureshit/113791653897019655)

---

## 2025-01-07T10:04:28.863Z

Day 367. The [#Azure](https://mastodon.social/tags/Azure) CLI command 'az resource show' can show you the properties of any Azure resource - well, almost any. Management groups are for some reason not supported. Seemingly the resource ID has to start with '/subscriptions'.

[View post](https://mastodon.social/@azureshit/113786504403885031)

---

## 2025-01-06T12:00:54.562Z

Day 366. After the failed deployment of the [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server from day 364, the server does not exist. The deployment never went through. Yet when switching the region because none of the availability zones in West Europe were supported, the Azure API seems to think that the server exists and denies to create a server with the same name name in a different region. It magically allowed us to do so after a few minutes again.

[View post](https://mastodon.social/@azureshit/113781299908340748)

---

## 2025-01-03T11:12:52.825Z

Day 365. When retrieving the list of available AKS versions in the [#Azure](https://mastodon.social/tags/Azure) CLI, the value for the 'isPreview' property is either true or null.

[View post](https://mastodon.social/@azureshit/113764124119635693)

---

## 2025-01-02T12:24:51.208Z

Day 364. It takes the [#Azure](https://mastodon.social/tags/Azure) API one minute to realize that the availability zone you are trying to deploy your Azure Database for PostgreSQL flexible server to is not supported in this region.

[View post](https://mastodon.social/@azureshit/113758744818540604)

---

## 2024-12-28T12:19:53.425Z

Day 363. The solution to the shit from day 339 is to chain your 'azurerm\_postgresql\_flexible\_server\_configuration' [#Terraform](https://mastodon.social/tags/Terraform) resources after each other and put some 'time\_sleep' resources in between. This way your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server won't be overwhelmed by having to update multiple configuration properties at once.

[View post](https://mastodon.social/@azureshit/113730413751353949)

---

## 2024-12-26T14:09:00.673Z

Day 362. When you're trying to create a resource of type "Microsoft.SaaS/resources" but did not yet register the corresponding provider, the [#Azure](https://mastodon.social/tags/Azure) API will tell you that your subscription is not registered for resources - which is really confusing.

[View post](https://mastodon.social/@azureshit/113719518210763204)

---

## 2024-12-25T22:48:21.170Z

Day 361. According to the [#Azure](https://mastodon.social/tags/Azure) CLI docs, the "capacity" argument is optional when creating a new capacity reservation, but if you omit it the CLI will tell you that its value is invalid.

[View post](https://mastodon.social/@azureshit/113715898034797543)

---

## 2024-12-23T08:38:32.287Z

Day 360. Once you have deleted a billing profile's invoice section you won't be able to create a new one with the same ID. This is the same behavior as for billing profiles themselves which we covered on day 286. But the error message is even more confusing: The [#Azure](https://mastodon.social/tags/Azure) API will tell you that the "sequence contains no matching element".

[View post](https://mastodon.social/@azureshit/113701231806769277)

---

## 2024-12-20T09:12:03.410Z

Day 359. [#Azure](https://mastodon.social/tags/Azure) tells us our VPN Gateway needs a larger subnet because it's zone-redundant, but actually it's on a SKU that does not support zone-redundancy. All we did was to swap the Basic SKU Public IP address to a Standard SKU Public IP address. We did not change the Gateway's SKU.

[View post](https://mastodon.social/@azureshit/113684376676401278)

---

## 2024-12-19T11:18:01.511Z

Day 358. Obviously the [#Azure](https://mastodon.social/tags/Azure) resource move operation is still ongoing, but the message makes it sound like it already succeeded.

[View post](https://mastodon.social/@azureshit/113679209691698037)

---

## 2024-12-18T12:43:18.069Z

Day 357. Deleting a subnet can sometimes fail due to an "retryable error", but the [#Azure](https://mastodon.social/tags/Azure) Portal does not give you any helpful information at all. And in case it wasn't obvious, neither did [#Microsoft](https://mastodon.social/tags/Microsoft)'s [#Copilot](https://mastodon.social/tags/Copilot) when you ask it to "troubleshoot" for you. The only reliable way to get debugging information is - as usual - to take a look at the failed API request.

[View post](https://mastodon.social/@azureshit/113673882701799358)

---

## 2024-12-17T09:27:09.404Z

Day 356. Is the amount of retention days for [#Azure](https://mastodon.social/tags/Azure) Log Analytics Workspaces supposed to be exactly 7 or between 30 to 730? We still don't know and Azure doesn't seem to know either.

[View post](https://mastodon.social/@azureshit/113667449120337633)

---

## 2024-12-16T09:11:19.237Z

Day 355. What is even more weird than the paywalled [#Azure](https://mastodon.social/tags/Azure) Bastion feature from day 352, is that you cannot disable certain features - for example copy & paste support - if you don't upgrade to a more expensive SKU.

[View post](https://mastodon.social/@azureshit/113661724539685839)

---

## 2024-12-14T12:28:53.837Z

Day 354. [#Azure](https://mastodon.social/tags/Azure) has comprehensive best practices on how to name your resources, including extensive documentation on how to abbreviate which resource types... just to throw all of that over board and require some resources to be named a specific way for them to work properly. For example, the subnet you put your Azure Bastion in must be named "AzureBastionSubnet".

[View post](https://mastodon.social/@azureshit/113651176822057476)

---

## 2024-12-13T13:43:41.709Z

Day 353. [#Microsoft](https://mastodon.social/tags/Microsoft) Cloud for Sustainability (MCFS) has a Developer Dashboard that allows you to try out the MCFS API in the browser. But apparently the backend does not send the correct CORS headers, so you can't actually try the API in the browser.

[View post](https://mastodon.social/@azureshit/113645808628866982)

---

## 2024-12-12T09:11:28.387Z

Day 352. [#Azure](https://mastodon.social/tags/Azure) Bastion is basically an overpriced jumphost VM but puts features that are pretty essential for a jumphost - for example to be able to connect from the CLI - behind more expensive SKUs for no apparent reason other than wanting to squeeze more money out of you.

[View post](https://mastodon.social/@azureshit/113639075897315485)

---

## 2024-12-11T12:25:59.710Z

Day 351. The [#Azure](https://mastodon.social/tags/Azure) CLI 'bastion' extension requires the 'ssh' extension to work. But instead of checking whether that extension has been installed, the CLI simply crashes if not.

[View post](https://mastodon.social/@azureshit/113634178478966193)

---

## 2024-12-10T10:31:24.531Z

Day 350. When you want to connect to a VM through [#Azure](https://mastodon.social/tags/Azure) Bastion in the Azure Portal, it asks you to upload your SSH Private Key File. That doesn't sound like a bad idea at all - especially given Microsoft's impeccable track record of never losing any keys.

[View post](https://mastodon.social/@azureshit/113628065596214740)

---

## 2024-12-09T09:38:23.409Z

Day 349. It takes up to 24 minutes to delete an [#Azure](https://mastodon.social/tags/Azure) CosmosDB for MongoDB account.

[View post](https://mastodon.social/@azureshit/113622194808739444)

---

## 2024-11-29T09:30:03.141Z

Day 348. It took the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider more than six months to support the latest [#MongoDB](https://mastodon.social/tags/MongoDB) versions after they have been released to Azure CosmosDB for MongoDB.

[View post](https://mastodon.social/@azureshit/113565538918894193)

---

## 2024-11-28T09:59:38.709Z

Day 347. When creating an [#Azure](https://mastodon.social/tags/Azure) Private DNS Resolver Inbound Endpoint through [#Terraform](https://mastodon.social/tags/Terraform) with the dynamic IP allocation method, the Terraform resource will not give you the endpoint's allocated IP address after it has been created. You will need to use a separate data source for the resource you just created to retrieve the IP address.

[View post](https://mastodon.social/@azureshit/113559992972389292)

---

## 2024-11-27T09:19:24.221Z

Day 346. Following up on the mandatory marketing opt-in in the [#Azure](https://mastodon.social/tags/Azure) Marketplace from day 345: The Azure Portal will send your contact information to a "main.prod.marketplaceleads.azure.com/api/leads" API endpoint which you can and should block in your browser's ad blocker, extending the filter list we posted on day 297.

[View post](https://mastodon.social/@azureshit/113554172426091759)

---

## 2024-11-26T10:53:30.827Z

Day 345. When you want to create a [#MongoDB](https://mastodon.social/tags/MongoDB) Atlas SaaS subscription in [#Azure](https://mastodon.social/tags/Azure), the Azure Portal won't let you proceed as long as you don't allow them to contact you with their marketing trash. Which is an optional step and totally not needed when creating these SaaS subscriptions per API.

[View post](https://mastodon.social/@azureshit/113548880171452369)

---

## 2024-11-25T11:30:57.058Z

Day 344. When importing an [#Azure](https://mastodon.social/tags/Azure) Public DNS Zone into the [#Terraform](https://mastodon.social/tags/Terraform) state, the import will fail if you use 'dnszones' instead of 'dnsZones' in the resource ID, even though that is exactly how the ID gets represented in the [#Azure](https://mastodon.social/tags/Azure) Portal's data model view.

[View post](https://mastodon.social/@azureshit/113543365070141199)

---

## 2024-11-24T10:42:35.457Z

Day 343. Sometimes it is not possible to delete an [#Azure](https://mastodon.social/tags/Azure) Kubernetes Service node pool because that would violate pod disruption budgets of workloads in that cluster. But when you try to delete that node pool through [#Terraform](https://mastodon.social/tags/Terraform), Terraform would not register that error and only time out after 60 minutes.

[View post](https://mastodon.social/@azureshit/113537512600536805)

---

## 2024-11-22T08:54:41.675Z

Day 342. Resources of type 'Microsoft.SaaS/resources' can only be deployed to the global location, but if you try to deploy them to a different region the [#Azure](https://mastodon.social/tags/Azure) API will make it sound like it's an provider registration issue.

[View post](https://mastodon.social/@azureshit/113525763713713743)

---

## 2024-11-21T08:55:46.481Z

Day 341. There are [#Azure](https://mastodon.social/tags/Azure) resources of type 'Microsoft.SaaS/resources' which are called SaaS subscriptions - which confusingly don't have anything to do with actual Azure subscriptions.

[View post](https://mastodon.social/@azureshit/113520105650777740)

---

## 2024-11-20T08:51:15.363Z

Day 340. We have reported a lot of shit regarding the [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server and its migration service. In the end we settled on doing our own data migration using "pgdump" so that we would not need to deal with the migration service's limitations and inconsistencies. But even this approach was unnecessarily complicated due to Azure deciding that on flexible server the Azure default user would now be named "azuresu" and no longer "azure\_superuser".

[View post](https://mastodon.social/@azureshit/113514425572410542)

---

## 2024-11-19T13:16:48.637Z

Day 339. Trying to update or delete multiple configuration resources of your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server at the same time? The server is not interested in that, it's already busy dealing with just one.

[View post](https://mastodon.social/@azureshit/113509807465096968)

---

## 2024-11-18T10:01:13.953Z

Day 338. Continuing the shit from day 337, when specifying [#Azure](https://mastodon.social/tags/Azure) plan "DevTest" for your new Azure subscription but the plan hasn't been enabled on your billing profile, the CLI will tell you that "no Azure plans are enabled" and you need to contact support. That is wrong, because the "Production" plan obviously is enabled.

[View post](https://mastodon.social/@azureshit/113503376110252935)

---

## 2024-11-16T13:45:40.246Z

Day 337. [#Azure](https://mastodon.social/tags/Azure) requires you to specify whether you will be running production or development workloads in your Azure subscription. You have to choose between one of two plans - "Production" and "DevTest". And apparently using "DevTest" will come with some discounts, but only when you have a Visual Studio subscription and only for certain services. That's so weirdly specific.

[View post](https://mastodon.social/@azureshit/113492934016535566)

---

## 2024-11-15T12:48:15.310Z

Day 336. To solve the mystery of our moveable but at the same time non-moveable IP addresses from day 333, to be able to actually move a Public IP address to another subscription it must not be associated with any other resource such as a load balancer or a VM. The docs only say that for when you want to move a VM, but it's applicable the other way around as well.

[View post](https://mastodon.social/@azureshit/113487045938885505)

---

## 2024-11-14T09:35:12.648Z

Day 335. Wow [#Microsoft](https://mastodon.social/tags/Microsoft), calm down. We know you love to shove your [#Copilot](https://mastodon.social/tags/Copilot) crap into whereever possible, but making it take up that much space in the [#Azure](https://mastodon.social/tags/Azure) Portal seems excessive.

[View post](https://mastodon.social/@azureshit/113480624547001032)

---

## 2024-11-12T23:01:39.558Z

Day 334. When deploying a VM Scale Set based on an [#Azure](https://mastodon.social/tags/Azure) Marketplace Image but you provide the wrong amount of data disks for that Image, the creation of the Scale Set in [#Terraform](https://mastodon.social/tags/Terraform) will fail, as we have seen on day 319. But guess what? The Scale Set in Azure stil got deployed, but is in some kind of failed provisioning state. Trying to re-run Terraform will result in Terraform failing because the remote resource already exists.

[View post](https://mastodon.social/@azureshit/113472471010842020)

---

## 2024-11-12T12:51:55.830Z

Day 333. Following up on the shit from day 332, apparently the [#Azure](https://mastodon.social/tags/Azure) Portal simply shows the "move" button for all resources, regardless of whether they can be moved or not. You will need to look into the docs to figure out which resources can be moved.

The weird thing is: Our IP addresses from day 332 are allegedly supported but moving still fails - and the linked article of course doesn't say anything about moving IP addresses.

[View post](https://mastodon.social/@azureshit/113470073459620948)

---

## 2024-11-12T12:51:39.832Z

Day 332. Public IP addresses cannot be moved to a different subscription, even though the [#Azure](https://mastodon.social/tags/Azure) Portal shows you the "move" button. And you'll only find out after you have been stuck in a validation process for five minutes.

[View post](https://mastodon.social/@azureshit/113470072410674760)

---

## 2024-11-08T10:10:47.073Z

Day 331. As we have covered before (shits from day 32, 121 & 311, for example), [#Azure](https://mastodon.social/tags/Azure) usually doesn't care about consistency in spelling of resource type names or resource ID segments, but don't YOU dare do that as well. You will immediately fail some arbitrary validation as seen here in the Azure [#Terraform](https://mastodon.social/tags/Terraform) provider.

[View post](https://mastodon.social/@azureshit/113446790566299791)

---

## 2024-11-07T09:09:45.246Z

Day 330. The [#Azure](https://mastodon.social/tags/Azure) Carbon Optimzation API is a fairly new service and still in preview, but even with completely new APIs Azure somehow manages to end up with POST endpoints for API endpoints that only return data and do not accept any payloads.

[View post](https://mastodon.social/@azureshit/113440888273231926)

---

## 2024-11-06T10:07:41.904Z

Day 329. To work around the missing data disk property from day 327, you could use the `azurerm\_virtual\_machine\_data\_disk\_attachment` [#Terraform](https://mastodon.social/tags/Terraform) resource to attach a data disk to a VM after it has been provisioned, but this does not work in case you are dealing with [#Azure](https://mastodon.social/tags/Azure) Marketplace VM images because they expect the data disks to be available on startup, as we covered on day 319.

[View post](https://mastodon.social/@azureshit/113435453810229140)

---

## 2024-11-05T14:48:23.360Z

Day 328. Following up on the shit from day 327, the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) maintainers acknowledged this issue but said that there's nothing they can do right now. At last partly because of the "behavior of the Azure API".

[View post](https://mastodon.social/@azureshit/113430895220691834)

---

## 2024-11-04T11:55:07.885Z

Day 327. Trying to deploy an [#Azure](https://mastodon.social/tags/Azure) Linux VM with a data disk attached through [#Terraform](https://mastodon.social/tags/Terraform)? Too bad, the Terraform resource 'azurerm\_linux\_virtual\_machine' resource does not support a data disks property, even though the predecessor 'azurerm\_virtual\_machine' did.

[View post](https://mastodon.social/@azureshit/113424551633350868)

---

## 2024-10-31T11:27:10.170Z

Day 326. Following up on the shit from day 325, the incorrect data model documentation is probably casued by the data model being so confusing that even [#Microsoft](https://mastodon.social/tags/Microsoft)'s technical writers mixed up [#Azure](https://mastodon.social/tags/Azure) Cognitive Services account SKU and Azure Cognitive Services account deployment SKU. Those are not the same and the account SKU actually is a letter+number code while the deployment SKU is not.

[View post](https://mastodon.social/@azureshit/113401792441078241)

---

## 2024-10-30T07:34:23.600Z

Day 325. We are pretty sure that the name of this [#Azure](https://mastodon.social/tags/Azure) Cognitive Services (or nowadays just Azure [#OpenAI](https://mastodon.social/tags/OpenAI)) account deployment is not a letter+number code, regardless of what the data model documentation says.

[View post](https://mastodon.social/@azureshit/113395214817422346)

---

## 2024-10-11T08:02:59.073Z

Day 324. Continuing the shit from day 319, not only do you need to somehow guess how many data disks are needed for your [#Azure](https://mastodon.social/tags/Azure) Marketplace VM image, you also need to know the exact disk sizes, otherwise Azure will always try to resize your disk on VM startup, which might fail.

[View post](https://mastodon.social/@azureshit/113287743344791573)

---

## 2024-10-10T07:24:17.808Z

Day 323. A recent update in the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider changed the format of the management group ID required for the "azurerm\_management\_group\_subscription\_association" resource. But the exported ID of pre-exisiting "azurerm\_management\_group" resources is still in the old format, resulting in errors when you want to associate an subscription with one of your management groups manged in Terraform.

[View post](https://mastodon.social/@azureshit/113281928908049289)

---

## 2024-10-09T07:17:27.915Z

Day 322. When you want to retrieve the IP addresses of your [#Azure](https://mastodon.social/tags/Azure) VM Scale Set in [#Terraform](https://mastodon.social/tags/Terraform), you need to use a data source and let it read attributes from the resource you just created, because the "azurerm\_virtual\_machine\_scale\_set" data source exports the instance IPs but the "azurerm\_virtual\_machine\_scale\_set" resource does not.

[View post](https://mastodon.social/@azureshit/113276239735163236)

---

## 2024-10-08T11:22:10.673Z

Day 321. To resolve the shit from day 319, the only way we found to reliably figure out how many data disks are needed for your [#Azure](https://mastodon.social/tags/Azure) Marketplace image is to try to deploy a VM using the "pre-set configuration" feature from the Azure Portal. From the resulting VM you can then retrieve the needed configuration parameters.

[View post](https://mastodon.social/@azureshit/113271539673821972)

---

## 2024-10-07T15:28:08.343Z

Day 320. Continuing the shit from day 319, not even [#Azure](https://mastodon.social/tags/Azure)'s built-in [#OpenAI](https://mastodon.social/tags/OpenAI) [#Copilot](https://mastodon.social/tags/Copilot) knows how many data disks your Azure Marketplace VM image needs. What was this thing supposed to be good for again?

[View post](https://mastodon.social/@azureshit/113266844520327293)

---

## 2024-10-04T07:32:12.948Z

Day 319. Trying to deploy an [#Azure](https://mastodon.social/tags/Azure) Marketplace VM image? Some VM images require your VM to have a specific amount of data disks present otherwise they refuse to start. But the Azure Marketplace does not give you any information on the required data disks, so it's more or less trial and error.

[View post](https://mastodon.social/@azureshit/113247986182039127)

---

## 2024-10-03T10:03:01.940Z

Day 318. Following up on the [#Azure](https://mastodon.social/tags/Azure) [#OpenAPI](https://mastodon.social/tags/OpenAPI) deployment SKUs that don't care about the instance's location, to ensure that your teams are not processing your sensitive data globally, additional to the 'location' property you will need to validate the 'Microsoft.CognitiveServices/accounts/deployments/sku.name' property. Azure luckily documents that, but still... shit.

[View post](https://mastodon.social/@azureshit/113242916908504747)

---

## 2024-10-02T15:06:42.285Z

Day 317. Even when specifying a non-global location for your [#Azure](https://mastodon.social/tags/Azure) [#OpenAI](https://mastodon.social/tags/OpenAI) instances, you are able to select a deployment SKU of type 'GlobalStandard' that will process your workloads globally. This makes this resource a nightmare to validate with Azure Policies, because you can't rely on a resource's location being its actual location anymore.

[View post](https://mastodon.social/@azureshit/113238448687041444)

---

## 2024-10-01T06:11:15.916Z

Day 316. We have covered this shit many times over the last year, but once again [#Azure](https://mastodon.social/tags/Azure) does not have free capacity in West Europe. This time we are not able to create new AKS clusters in Standard SKU.

[View post](https://mastodon.social/@azureshit/113230680943071453)

---

## 2024-09-30T07:24:24.046Z

Day 315. When migrating our [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL single server to flexible server using Azure's migration service, our database ended up in a state that is not documented in the list of possible states.

[View post](https://mastodon.social/@azureshit/113225306212891965)

---

## 2024-09-27T07:56:04.086Z

Day 314. To work around the shit from day 313, you will need to use an [#Azure](https://mastodon.social/tags/Azure) "azurerm\_public\_ip" [#Terraform](https://mastodon.social/tags/Terraform) data source that retrieves the allocated Public IP address after the VM has been provisioned and use the attributes of that data source for your DNS record.

[View post](https://mastodon.social/@azureshit/113208443802997767)

---

## 2024-09-26T07:52:35.828Z

Day 313. When you have an [#Azure](https://mastodon.social/tags/Azure) "azurerm\_public\_ip" [#Terraform](https://mastodon.social/tags/Terraform) resource with dynamic allocation mode that then gets assigned to an VM, Terraform only retrieves the resulting IP address when applying Terraform after the VM has been fully provisioned. This means that you cannot create both a VM and a DNS record for that IP address in the same Terraform apply run (even when making the DNS record dependent on the VM), because Terraform won't have the IP address for the DNS record during that run.

[View post](https://mastodon.social/@azureshit/113202767844041815)

---

## 2024-09-25T07:13:51.746Z

Day 312. You want migrate your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL single server to flexible server using the migration service? That is possible without downtime, but only if you pay for the more expensive SKUs. Burstable SKU is not supported, except in West Europe for some reason.

[View post](https://mastodon.social/@azureshit/113196953222720743)

---

## 2024-09-24T06:44:52.390Z

Day 311. When migrating your [#Azure](https://mastodon.social/tags/Azure) Databse for PostgreSQL single server to flexible server using Azure's migration service, the target DB has location "France Central" when the source DB has location "francecentral". Obviously that's the same thing, but nobody over at [#Microsoft](https://mastodon.social/tags/Microsoft) seems to get paid to pay attention to data model consistency.

[View post](https://mastodon.social/@azureshit/113191176921638579)

---

## 2024-09-23T07:17:14.231Z

Day 310. When trying to migrate your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL single server instance to a flexible server instance, the docs tell you to supply the parameter value "Online" when you want to perform an online migration, but of course that value is not supported and you need to spell it differently.

[View post](https://mastodon.social/@azureshit/113185641871836063)

---

## 2024-09-20T07:18:39.777Z

Day 309. Following up on the shit from day 308, you could argue that the "az billing profile" command is still in preview and therefor it's okay for it to not support all properties or functionalities yet. But this command has been introduced four years ago and has been in preview ever since.

[View post](https://mastodon.social/@azureshit/113168660547058125)

---

## 2024-09-19T15:45:50.100Z

Day 308. When trying to create [#Azure](https://mastodon.social/tags/Azure) billing profiles through the CLI you are not able to specify a billing profile's invoice recipient email addresses. You would need to directly do API calls to update that property.

[View post](https://mastodon.social/@azureshit/113164992518441108)

---

## 2024-09-18T21:46:53.823Z

Day 307. [#Microsoft](https://mastodon.social/tags/Microsoft)'s Cloud for Sustainability API can in theory provide emissions data for customer workloads - which is great - but that API is not available for [#Azure](https://mastodon.social/tags/Azure) customers billed through a third party CSP - which is shit.

[View post](https://mastodon.social/@azureshit/113160749961679731)

---

## 2024-09-17T06:59:52.048Z

Day 306. Following up on the shit from day 305, to be fair, they probably did that change because the [#Azure](https://mastodon.social/tags/Azure) REST API supports more values for the "privateEndpointNetworkPolicies" property than just "Enabled" and "Disabled". But even after the change the [#Terraform](https://mastodon.social/tags/Terraform) provider still does only support two of those.

[View post](https://mastodon.social/@azureshit/113151599708949562)

---

## 2024-09-16T08:08:10.696Z

Day 305. Recently the [#Azure](https://mastodon.social/tags/Azure) Terraform Provider renamed the property "private\_endpoint\_network\_policies\_enabled" in the "azurerm\_subnet" resource to "private\_endpoint\_network\_policies" and its value can now be either "Enabled" or "Disabled". Which would make total sense if it weren't for all the other properties in that resource continuing to represent enabled states with true or false.

[View post](https://mastodon.social/@azureshit/113146206007462690)

---

## 2024-09-13T22:37:56.394Z

Day 304. The shit from day 303 led us to check out the [#Azure](https://mastodon.social/tags/Azure) Ubuntu Mirrors and... we couldn't really make sense of that "/ubuntu/ubuntu/ubuntu/ubuntu/..." directory structure. But hey, it ain't stupid if it wor... - wait, it didn't.

[View post](https://mastodon.social/@azureshit/113132639117807141)

---

## 2024-09-12T13:14:34.307Z

Day 303. A few weeks ago, our [#Azure](https://mastodon.social/tags/Azure) VMs weren't able to start because the Azure Ubuntu Mirrors were unavailable. They magically worked again after a few hours.

[View post](https://mastodon.social/@azureshit/113124761553454030)

---

## 2024-09-11T07:46:51.808Z

Day 302. [#Azure](https://mastodon.social/tags/Azure) service tags represent IP ranges of Azure services and allow you to configure networking (for example routes) for those services. But you better don't try to configure Azure Firewall rules with these service tags. You obviously need to use Virtual Network service tags for that, which only support a subset of Azure services supported by service tags.

[View post](https://mastodon.social/@azureshit/113117810642315112)

---

## 2024-09-10T14:33:18.265Z

Day 301. [#Azure](https://mastodon.social/tags/Azure) decided to rename the default "azure\_superuser" in Database for PostgreSQL single server (which is being retired) to "azuresu" in the newer Database for PostgreSQL flexible server offering. This means that you can't reuse your PostgreSQL dumps to restore data in flexible server.

[View post](https://mastodon.social/@azureshit/113113746522796050)

---

## 2024-09-09T08:17:28.340Z

Day 300. The [#Azure](https://mastodon.social/tags/Azure) Portal can't even show a subscription anymore without crashing. Clearing browser data helps, but only temporarily.

[View post](https://mastodon.social/@azureshit/113106606380603173)

---

## 2024-09-06T08:36:07.406Z

Day 299. Following up on the shit from day 288, there is a way to log in to the CLI with a principal when it is not assigned on any subscriptions: You can supply the argument "--allow-no-subscriptions". Still, this is an inconvenience. You can actually see that this is likely something they hacked into their "everything is centered around a subscription" approach because the CLI still wants to show you a subscription but simply names it "N/A(tenant level account)". via [@easimon](https://mastodon.social/@easimon)

[View post](https://mastodon.social/@azureshit/113089692788467302)

---

## 2024-09-05T19:22:12.384Z

Day 298. After hastily recalling its controversial Recall feature because it was deemed a security and privacy nightmare, after everybody has calmed down and moved on two months later, [#Microsoft](https://mastodon.social/tags/Microsoft) decided to reintroduce it without telling anybody what they actually changed about it. But they promised they will do that later and why wouldn't we trust them on that?

[View post](https://mastodon.social/@azureshit/113086570977026143)

---

## 2024-09-03T07:04:19.820Z

Day 297. Following up on the usage information collecting shit from day 296, you can deny this behavior by simply letting your browser block API requests used for telemetry data, for example API requests to the URL "portal.azure.com/api/Telemetry".

[View post](https://mastodon.social/@azureshit/113072344912023206)

---

## 2024-09-02T05:32:07.488Z

Day 296. The [#Azure](https://mastodon.social/tags/Azure) Portal collects a lot of your usage information and sends it home to [#Microsoft](https://mastodon.social/tags/Microsoft). This even includes what buttons you click in the portal.

[View post](https://mastodon.social/@azureshit/113066320034626058)

---

## 2024-08-30T07:11:29.957Z

Day 295. Following up on the shit from day 242, the reason the error details do not get shown when a [#Terraform](https://mastodon.social/tags/Terraform) resource deployment gets denied by an [#Azure](https://mastodon.social/tags/Azure) Policy is that the Azure Terraform Provider chooses to simply omit the additional information and to only display the error message instead of the whole error response.

[View post](https://mastodon.social/@azureshit/113049723860071473)

---

## 2024-08-29T08:40:16.200Z

Day 294. The [#Azure](https://mastodon.social/tags/Azure) CLI's 'az billing subscription update' command does not allow you specifying a subscription ID but instead will always take the default subscription selected in your CLI configuration. This behavior is totally out of line with all other CLI commands and not documented anywhere. If your default subscription is not eligble to be maintained as direct billing subscription, the CLI will simply tell you 'resource could not be found'.

[View post](https://mastodon.social/@azureshit/113044410610334567)

---

## 2024-08-28T07:41:27.971Z

Day 293. According to the [#Azure](https://mastodon.social/tags/Azure) CLI documentation of the latest version, you can use "az alias" to manage subscription aliases. But when trying that in the latest version, it says the command does not exist. The correct command would be "az account alias".

[View post](https://mastodon.social/@azureshit/113038517073801260)

---

## 2024-08-27T05:29:27.057Z

Day 292. Somehow when using [#Azure](https://mastodon.social/tags/Azure)'s "azapi" Terraform Provider with the Microsoft.Billing REST API, when you're not paying attention, you are able to import the full list of invoice sections for a billing profile into your Terraform state as individual invoice section resource. But you'd only shoot yourself in the foot by doing so because now the Terraform provider performs invalid API requests and the API only responds with error 405.

[View post](https://mastodon.social/@azureshit/113032335658448513)

---

## 2024-08-25T22:45:57.245Z

Day 291. The shit with the read-only properties of the [#Azure](https://mastodon.social/tags/Azure) Billing Subscriptions REST API from day 290 might be due to the API only allowing PATCH requests which might be not supported by the azapi Terraform provider. But we don't know for sure since there is no documentation on this and apparently nobody else on the Internet is insane enough to actually try to automate their billing setup on Azure.

[View post](https://mastodon.social/@azureshit/113025086733832062)

---

## 2024-08-25T15:53:50.962Z

Day 290. When trying to use the [#Azure](https://mastodon.social/tags/Azure) Billing Subscriptions REST API, the azapi Terraform provider will tell you that the property `properties` is read-only, even though the API documentation clearly states that there are properties you can update.

[View post](https://mastodon.social/@azureshit/113023466272160595)

---

## 2024-08-22T09:05:35.345Z

Day 289. Need help from [#Azure](https://mastodon.social/tags/Azure) support? Sure, no worrie.... oh noo, the Portal crashed :(

[View post](https://mastodon.social/@azureshit/113004873996043124)

---

## 2024-08-21T08:07:11.172Z

Day 288. We have an [#Azure](https://mastodon.social/tags/Azure) Service Principal that is Billing Account Administrator for our Azure tenant and use it to create billing profiles and subscriptions automatically. But using that principal to log in to the Azure CLI fails because the CLI always expects the principal to be assigned to at least one subscription - which is totally not needed for our use case. So much for principle of least privilege.

[View post](https://mastodon.social/@azureshit/112998982036151873)

---

## 2024-08-20T19:16:04.032Z

Day 287. Trying to update existing [#Azure](https://mastodon.social/tags/Azure) billing profiles through the CLI? Both the create and update commands will fail if you supply the "--enabled-azure-plans" argument because "disabling plans is not supported".

[View post](https://mastodon.social/@azureshit/112995949869992878)

---

## 2024-08-19T07:46:54.357Z

Day 286. After you have finally managed to delete an [#Azure](https://mastodon.social/tags/Azure) billing profile, you are no longer able to create a new one with the same name. Azure would give you a cryptic and not at all helpful error message that says "The resource or one of its dependencies could not be found".

[View post](https://mastodon.social/@azureshit/112987577670223514)

---

## 2024-08-17T00:30:36.258Z

Day 285. Sometimes your [#Azure](https://mastodon.social/tags/Azure) Firewall ends up without a private IP address. How would networking work in that case? Luckily this Firewall is in a failed provisioning state anyways, so you don't really need to care.

[View post](https://mastodon.social/@azureshit/112974537441734305)

---

## 2024-08-15T11:13:22.703Z

Day 284. Continuing the shit with the broken "Microsoft.Billing" [#Azure](https://mastodon.social/tags/Azure) resource provider API from day 283: Invoice sections are not the only resource affected. We observed the exact same behavior at least for billing profiles themselves. The public APIs are so broken that you need to use private preview API versions - which are not officially supported - to get this shit working.

[View post](https://mastodon.social/@azureshit/112965740310997339)

---

## 2024-08-14T07:33:25.032Z

Day 283. Continuing the shit from day 282, to delete an [#Azure](https://mastodon.social/tags/Azure) billing profile invoice section you suddenly need to use API version "2020-11-01-privatepreview" which according to the API specs is not even officially supported for the "Microsoft.Billing" resource provider. Therefor it cannot be used for example for resource creation with "azapi" Terraform provider except when you explicitly disable schema validation.

[View post](https://mastodon.social/@azureshit/112959213078424390)

---

## 2024-08-13T21:23:17.326Z

Day 282. Following up on the shit from day 280. When then using [#Azure](https://mastodon.social/tags/Azure) API version "2020-05-01", you can create billing profile invoice sections, but you cannot delete them because "the resource does not support the API version".

[View post](https://mastodon.social/@azureshit/112956813955704403)

---

## 2024-08-09T08:13:31.699Z

Day 281. When creating a [#Azure](https://mastodon.social/tags/Azure) Billing Profile Invoice Section through the azapi Terraform resource (which you have to because it is not supported by the azurerm provider), the resource will for some reason have a double "//" in its ID. An ID like this is invalid and cannot get supplied to a subscription resource.

[View post](https://mastodon.social/@azureshit/112931059249558519)

---

## 2024-08-08T07:50:06.930Z

Day 280. The [#Azure](https://mastodon.social/tags/Azure) REST API documentation tells you to use API version "2024-04-01" when creating billing profile invoice sections, but this version is not supported. You have to use either version "2020-05-01" or some private preview versions.

[View post](https://mastodon.social/@azureshit/112925304876313354)

---

## 2024-08-07T06:54:55.636Z

Day 279. If you deploy an [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server through [#Terraform](https://mastodon.social/tags/Terraform) and allow Azure to choose the availability zone in the hopes that it chooses one that actually has capacity available, the Azure Terraform Provider will try to replace the zone chosen on server side with "null" on every run unless you explicitly ignore it.

[View post](https://mastodon.social/@azureshit/112919425556320862)

---

## 2024-08-06T09:31:46.553Z

Day 278. Continuing on the shit from day 277, the US State Department was only able to discover the [#Microsoft](https://mastodon.social/tags/Microsoft) Exchange Online hack because they purchased a premium logging feature which normally is not accessible to customers.

[View post](https://mastodon.social/@azureshit/112914380000433527)

---

## 2024-08-05T06:48:44.001Z

Day 277. When [#Microsoft](https://mastodon.social/tags/Microsoft) Exchange Online got hacked last year, Microsoft did not even notice it on their own. The attack only got discovered because the US State Department noticed unusual activities in their mailboxes and then alerted Microsoft.

[View post](https://mastodon.social/@azureshit/112908076580747586)

---

## 2024-08-02T22:55:16.256Z

Day 276. Continuing the shit from day 274, the community reacted to this announcement exactly as you would expect. Rightfully complaining about the short transition windows, unclear migration docs and now unsupported features that were previuosly supported.

[View post](https://mastodon.social/@azureshit/112894890230080005)

---

## 2024-08-01T07:59:32.587Z

Day 275. The new [#Teams](https://mastodon.social/tags/Teams) Workflows that replace the hastily retired Office 365 connectors (see shit from day 273) do not support utilization of any kind of technical users. Meaning the workflow will always get owned by an individual user of your organization - and get orphaned if that user leaves.

[View post](https://mastodon.social/@azureshit/112885705774142887)

---

## 2024-07-31T07:10:42.629Z

Day 274. [#Microsoft](https://mastodon.social/tags/Microsoft) has had so many security breaches over the last year that you can't even keep track anymore. What was this one about again?

[View post](https://mastodon.social/@azureshit/112879851445725620)

---

## 2024-07-30T15:14:57.792Z

Day 273. [#Microsoft](https://mastodon.social/tags/Microsoft) decided to retire the Teams Office 365 connectors (which many organizations use for example for alerting) with only 6 weeks notice. The alternative, Teams Workflows, is currently not fully supported by most tools such as Grafana and alertmanager.

[View post](https://mastodon.social/@azureshit/112876093295095280)

---

## 2024-07-24T11:09:00.454Z

Day 272. [#HashiCorp](https://mastodon.social/tags/HashiCorp) engineers maintaing the [#Azure](https://mastodon.social/tags/Azure) Terraform Providers have opened an issue for the broken group ownership validation (shit from day 271) in the Microsoft Graph GitHub repository back in 2021. Guess how many Microsoft engineers have since responded to it? None.

[View post](https://mastodon.social/@azureshit/112841152295841996)

---

## 2024-07-23T07:50:48.183Z

Day 271. The shit from day 270 is a bug in the [#Microsoft](https://mastodon.social/tags/Microsoft) Graph API. HashiCorp engineers have essentially made their peace with that shitty API and just moved on.

[View post](https://mastodon.social/@azureshit/112834710613507736)

---

## 2024-07-22T07:47:29.438Z

Day 270. Service Principals are valid Owners of [#Azure](https://mastodon.social/tags/Azure) AD groups. If a service principal creates a group, it will be the single Owner of the group. But if you have a User and a Service Principal as Owner, you can't remove the User because "The group must have at least one owner, hence this owner cannot be removed".

[View post](https://mastodon.social/@azureshit/112829035277613892)

---

## 2024-07-21T13:18:58.344Z

Day 269. Funnily enough, if you've accidentally triggered the suicidal CLI command from day 266, the CLI will delete one role assignment after another (probably sorted by UUID or something stupid like that) and if it deletes your own role assignment before the others, the process will kill itself since it does not have sufficient permission anymore.

[View post](https://mastodon.social/@azureshit/112824676407055497)

---

## 2024-07-19T08:00:11.427Z

Day 268. If your flight got delayed yesterday, that's because [#Azure](https://mastodon.social/tags/Azure) suffered yet another outage of multiple of its services in the US.

[View post](https://mastodon.social/@azureshit/112812098282928540)

---

## 2024-07-18T07:11:00.558Z

Day 267. "You're [#Azure](https://mastodon.social/tags/Azure) tenant might have different semantics" is probably one of the worst things you could ever hear from a [#Microsoft](https://mastodon.social/tags/Microsoft) employee when trying to troubleshoot Azure problems.

[View post](https://mastodon.social/@azureshit/112806242585678897)

---

## 2024-07-17T06:38:05.236Z

Day 266. Trying to delete a role assignment through the [#Azure](https://mastodon.social/tags/Azure) CLI but forgot to specify arguments? The CLI will conveniently offer you to simply delete every single role assignment on the entire subscription.

[View post](https://mastodon.social/@azureshit/112800450820911511)

---

## 2024-07-16T07:33:36.762Z

Day 265. We would allow [#Microsoft](https://mastodon.social/tags/Microsoft) to use the content of this account to train their shitty AI products, but Microsoft's AI CEO (whatever that is) apparently already thinks it would be okay to just steal it, so nevermind.

[View post](https://mastodon.social/@azureshit/112795006845368487)

---

## 2024-07-15T07:21:27.755Z

Day 264. Shit like the one from day 263 is why it is so hard to design [#Azure](https://mastodon.social/tags/Azure) Policies. They will sometimes only work for specific clients using specific API versions, giving you the illusion of security. You have to test your policies against every possible client for every possible data model of every API version to actually ensure that they work as intended.

[View post](https://mastodon.social/@azureshit/112789296758648261)

---

## 2024-07-14T14:27:12.796Z

Day 263. Following up on the shit from day 252, even though the role assignment scope is not part of the request body in newer API versions, the [#Azure](https://mastodon.social/tags/Azure) Portal uses an outdated API version where it was still optional to supply in the request body. That's why Azure Policies checking for the "Microsoft.Authorization/roleAssignments/scope" alias will work for the Portal but not for any other client using a newer API version.

[View post](https://mastodon.social/@azureshit/112785308568160892)

---

## 2024-07-11T07:54:57.830Z

Day 262. Following up on the shit from day 261, the reason for that is that the [#Azure](https://mastodon.social/tags/Azure) API simply always return status code 204 when deleting an Azure Policy assignment, even if there is no assignment with that ID.

[View post](https://mastodon.social/@azureshit/112766779249558885)

---

## 2024-07-10T08:06:37.128Z

Day 261. When deleting [#Azure](https://mastodon.social/tags/Azure) Policy assignments through the Azure CLI, the CLI will happily swallow whatever assignment names you give to it and never return any errors or indicate that an assignment like this doesn't even exist.

[View post](https://mastodon.social/@azureshit/112761162767745543)

---

## 2024-07-08T20:41:21.074Z

Day 260. [#Azure](https://mastodon.social/tags/Azure) has begun forcing its Copilot crap onto Azure Portal users. But it can't actually do anything besides generating responses every other LLM could generate for you. It being there doesn't really add any value for users at all.

[View post](https://mastodon.social/@azureshit/112752805876249113)

---

## 2024-07-06T09:43:58.836Z

Day 259. Deletion of an [#Azure](https://mastodon.social/tags/Azure) CosmosDB account failed but it only shows you a cryptic error code instead of a helpful message.

[View post](https://mastodon.social/@azureshit/112738896368824271)

---

## 2024-07-05T09:36:02.174Z

Day 258. Contrary to what the name indicates, regional [#Azure](https://mastodon.social/tags/Azure) VMs are not actually zone-redundant. They simply exist within one availability zone of that region and if that zone goes down, they go down. You need to select the "availability zone" availability option for your VM to get deployed rendundantly across multiple zones in a region.

[View post](https://mastodon.social/@azureshit/112733202819993372)

---

## 2024-07-04T18:33:17.700Z

Day 257. When you create an [#Azure](https://mastodon.social/tags/Azure) Policy to deny role assignments and assign it to a management group, it will only deny role assignments on resources under that management group, but not on the management group itself.

[View post](https://mastodon.social/@azureshit/112729653097051185)

---

## 2024-07-03T10:59:33.702Z

Day 256. The [#Azure](https://mastodon.social/tags/Azure) Advisor recommends you to "migrate your VMs to an availability zone" which is confusing and misleading. What they actually mean is migrating the VM to enable "availability zone support" which then allows you to deploy your VM redundantly across multiple availability zones (and obviously gives Microsoft more $$$).

[View post](https://mastodon.social/@azureshit/112722206634712117)

---

## 2024-07-02T09:26:48.538Z

Day 255. We have no idea what went wrong during this deployment of an [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL single server. But believe us, we did not try to name our database user "The user name conflict with an existing database user name".

[View post](https://mastodon.social/@azureshit/112716179605686385)

---

## 2024-07-01T08:12:04.919Z

Day 254. Following up the unavailable resource provider from day 250. It took [#Azure](https://mastodon.social/tags/Azure) almost two days to roll out a fix and while they confirmed to us in a support ticket that they were experiencing issues on their side, somehow they never got around to update their useless status dashboard and until now have not publicly recognized the downtime.

[View post](https://mastodon.social/@azureshit/112710223456873913)

---

## 2024-06-29T21:25:19.833Z

Day 253. The [#Azure](https://mastodon.social/tags/Azure) Portal is supplying two different API versions to the Azure REST API when creating role assignments. One of which doesn't even exist for the "Microsoft.Authorization" resource provider.

[View post](https://mastodon.social/@azureshit/112702018016313673)

---

## 2024-06-28T07:47:36.538Z

Day 252. Continuing the shit from day 251. There is an [#Azure](https://mastodon.social/tags/Azure) Policy alias called "Microsoft.Authorization/roleAssignments/scope", but it's always null if the API client does not voluntarily supply a "scope" property in the request payload. This problem is not documented anywhere and you have to stumble over a years-old GitHub issue where a Microsoft employee admits that the alias is basically not working at all.

[View post](https://mastodon.social/@azureshit/112693140293857686)

---

## 2024-06-27T07:50:42.583Z

Day 251. There is no way to deny role assigments with a specifc scope using [#Azure](https://mastodon.social/tags/Azure) Policies. That is because the role assignment scope property only exists in older API versions (where it was optional) and in newer API versions exclusively gets specified in the request URI - which an Azure Policy cannot evaluate.

[View post](https://mastodon.social/@azureshit/112687490176193392)

---

## 2024-06-26T09:11:27.946Z

Day 250. The [#Azure](https://mastodon.social/tags/Azure) 'Microsoft.Security' resource provider has continuously been unavailable for the last two days, resulting in you not being able to read or modify your subscription's security contacts. Microsoft only got around to fix this issue a couple of hours before posting this shit.

[View post](https://mastodon.social/@azureshit/112682145411513898)

---

## 2024-06-25T07:27:11.758Z

Day 249. Continuing the shit from day 246 with the multiple [#Azure](https://mastodon.social/tags/Azure) AD Entra ID security groups with the same name, in this thread you have Microsoft employees arguing whether that is a fault on the API side or in the client. Nobody seems to know how security groups actually should behave: Is the name supposed to be unique or not?

[View post](https://mastodon.social/@azureshit/112676073095546716)

---

## 2024-06-24T08:29:07.546Z

Day 248. Deployment of an [#Azure](https://mastodon.social/tags/Azure) App Service Hosting environment can take up to almost 4 hours.

[View post](https://mastodon.social/@azureshit/112670654302950069)

---

## 2024-06-18T06:15:23.333Z

Day 247. The client-side check from day 246 is even shittier than you might think. The [#Azure](https://mastodon.social/tags/Azure) Portal makes an API request using the Graph API, searching for groups with the name you are trying to use. If it finds any groups, it tells you that you cannot create a group with that name. In this screenshot you can see the Graph API returning MULTIPLE groups with the exact same name and the Portal still determining that it's not a valid name.

[View post](https://mastodon.social/@azureshit/112636154565701376)

---

## 2024-06-17T09:05:39.895Z

Day 246. The [#Azure](https://mastodon.social/tags/Azure) Portal does not allow you to create an Azure Entra ID security group when a group with that display name already exists, but that check is entirely client-side. Using the API you are able to create multiple groups with the same display name.

[View post](https://mastodon.social/@azureshit/112631161808017797)

---

## 2024-06-04T07:37:04.566Z

Day 245. When replacing the user-assigned identity of an [#Azure](https://mastodon.social/tags/Azure) Container Registry through [#Terraform](https://mastodon.social/tags/Terraform), the ACR will simply keep both identities, even if the old one has already been deleted.

[View post](https://mastodon.social/@azureshit/112557203427408477)

---

## 2024-06-03T09:09:13.963Z

Day 244. Remember the shit from day 213, where [#Azure](https://mastodon.social/tags/Azure) wanted you to download some random PowerShell scripts and provide them to your Data Factory? They recently updated the documentation and while they still tell you that you need these files, the download links have disappeared. That's actually a great move, because this saves you from wasting your time on this broken product since you now can't even try to setup custom DNS for your ADF SSIS-IR.

[View post](https://mastodon.social/@azureshit/112551903491331641)

---

## 2024-05-31T08:05:18.916Z

Day 243. Update regarding the arbitrary intransparent [#Azure](https://mastodon.social/tags/Azure) Firewall Rule Collection Group size limits from day 141. With API version "2023-05-01" (which hit the stable channel end of August 2023) they have added a way to query the rule collection group size through the REST API. However, the size is still not visible in any other clients.

[View post](https://mastodon.social/@azureshit/112534665226751471)

---

## 2024-05-30T12:54:26.771Z

Day 242. Creation of an [#Azure](https://mastodon.social/tags/Azure) resource got denied by an Azure Policy and the API response tells you to check the error details for the policy IDs and then proceeds to not give you any error details. This only happens for some Azure Policies and so far we haven't been able to figure out why.

[View post](https://mastodon.social/@azureshit/112530139825183227)

---

## 2024-05-29T07:57:04.653Z

Day 241. The [#Azure](https://mastodon.social/tags/Azure) Advisor warns us that this Azure Marketplace VM image has been deprecated but at the same time they acknowledge that there is no newer version available.

[View post](https://mastodon.social/@azureshit/112523308213983231)

---

## 2024-05-28T21:03:14.456Z

Day 240. The [#Azure](https://mastodon.social/tags/Azure) Advisor shows us recommendations for some virtual machines, but apparently doesn't even know the subscription some of these VMs are in.

[View post](https://mastodon.social/@azureshit/112520737223689328)

---

## 2024-05-27T08:35:07.866Z

Day 239. When deploying ARM templates in the [#Azure](https://mastodon.social/tags/Azure) Portal, the wizard shows you both region and location but does not explain what that means and why they are different.

[View post](https://mastodon.social/@azureshit/112512133225844694)

---

## 2024-05-26T08:50:57.986Z

Day 238. Zone-redundant HA deployments of [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server are for some reason not supported in West Europe. The docs say that's only temporarily while existing deployments continue to exist. But we haven't been able to deploy such a database in over 5 months.

[View post](https://mastodon.social/@azureshit/112506533182474206)

---

## 2024-05-25T08:37:37.104Z

Day 237. If you delete your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server instance and then recreate it quickly after, Azure will tell you that "Operations on a server group in dropping state are not allowed". If it's not yet deleted, why do you confirm its deletion?

[View post](https://mastodon.social/@azureshit/112500818385325496)

---

## 2024-05-24T15:25:53.188Z

Day 236. [#Azure](https://mastodon.social/tags/Azure) virtual machines still don't support ED25519 SSH key formats which have been around for more than 10 years now and have been adopted by all major cloud providers.

[View post](https://mastodon.social/@azureshit/112496761449943583)

---

## 2024-05-23T07:29:18.620Z

Day 235. [#Azure](https://mastodon.social/tags/Azure) seemingly once again has capacity problems in West Europe.

[View post](https://mastodon.social/@azureshit/112489225166374481)

---

## 2024-05-22T10:54:15.775Z

Day 234. In the Compliance view of [#Azure](https://mastodon.social/tags/Azure) Policies, the Azure Portal does not allow you to open resource in a new tab. And if you open a resource to see their compliance state and then go back to your policy view, the Portal resets all of your filters.

[View post](https://mastodon.social/@azureshit/112484368762294389)

---

## 2024-05-21T07:55:13.932Z

Day 233. Because [#Microsoft](https://mastodon.social/tags/Microsoft) apparently refused cooperation after the Microsoft Exchange Online hack last year, Germany's federal agency for IT-Security has to sue Microsoft to get them to hand over more details related to that security incident.

[View post](https://mastodon.social/@azureshit/112478002474452874)

---

## 2024-05-20T05:58:33.611Z

Day 232. When you export logs from an [#Azure](https://mastodon.social/tags/Azure) Log Analytics Workspace, in the CSV file the logs will get sorted by category name and only after that by timestamp.

[View post](https://mastodon.social/@azureshit/112471881390736191)

---

## 2024-05-19T10:31:14.899Z

Day 231. Reading alerts in the [#Azure](https://mastodon.social/tags/Azure) Portal failed with "Error: ".

[View post](https://mastodon.social/@azureshit/112467291333833063)

---

## 2024-05-18T09:25:50.850Z

Day 230. You can specify the location for your [#Azure](https://mastodon.social/tags/Azure) Application Insights resource, but Application Insights will in turn create an action group in the "global" location, regardless of the location you specified for Application Insights and there is no way to change that.

[View post](https://mastodon.social/@azureshit/112461371857134284)

---

## 2024-05-17T08:09:41.356Z

Day 229. [#Microsoft](https://mastodon.social/tags/Microsoft) had no automated rotation process for their Microsoft Services Account signing keys and did not once rotate any keys since 2021. This allowed attackers in the Microsoft Exchange Online hack last year to utilize a key from 2016!

[View post](https://mastodon.social/@azureshit/112455410080328004)

---

## 2024-05-16T09:02:08.861Z

Day 228. The VM instance affected by the "InternalExecutionError" from day 227 ended up in a failed provisioning state but at the same time is running and still healthy?

[View post](https://mastodon.social/@azureshit/112449954045075939)

---

## 2024-05-15T08:05:59.540Z

Day 227. Reimaging instances of an [#Azure](https://mastodon.social/tags/Azure) VMSS just failed with an "InternalExecutionError", but also status code "200 OK".

[View post](https://mastodon.social/@azureshit/112444070922589490)

---

## 2024-05-14T07:55:56.611Z

Day 226. Following up on day 220, deleting the firewall rule of the Azure Database for PostgreSQL single server failed because we had set the public network access for the database to disabled. Apparently, if public network access is not enabled, the API no longer allows you to modify or delete firewall rules, even though the firewall rules still exist.

[View post](https://mastodon.social/@azureshit/112438369186943257)

---

## 2024-05-13T07:32:57.986Z

Day 225. [#Microsoft](https://mastodon.social/tags/Microsoft) claimed that they figured out how the attackers got their hands on the signing key in the [#Microsoft](https://mastodon.social/tags/Microsoft) Exchange Online hack last year, but their statement was completely made up and they only corrected it over 6 months later.

[View post](https://mastodon.social/@azureshit/112432616438584020)

---

## 2024-05-11T06:54:23.782Z

Day 224. Leave it to Microsoft's login frontends to make the wrong requests to their own backends.

[View post](https://mastodon.social/@azureshit/112421140154390672)

---

## 2024-05-10T07:13:29.216Z

Day 223. Some [#Azure](https://mastodon.social/tags/Azure) PaaS resource names are arbitrarily limited to 24 characters while others are not. This makes it really hard to implement consistent naming conventions, even the ones recommended by Azure. (via [@ducksauz](https://snug.town/@ducksauz) [@zhaph](https://fosstodon.org/@zhaph))

[View post](https://mastodon.social/@azureshit/112415552910836686)

---

## 2024-05-09T11:35:07.793Z

Day 222. The CSRB's findings on the [#Microsoft](https://mastodon.social/tags/Microsoft) Exchange Online intrusion last year are so bad that they recommended to Microsoft to stop building shit products until "substantial security improvements have been made". Expect more content on that report in the future.

[View post](https://mastodon.social/@azureshit/112410919422504897)

---

## 2024-05-08T06:59:17.301Z

Day 221. Continuing the shit from day 220, because firewall rules for your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL single server are dedicated [#Terraform](https://mastodon.social/tags/Terraform) resources, disabling public network access and deleting firewall rules for your database in Terraform can result in a race condition: If public network access gets disabled before the firewall rules have been deleted, you are no longer allowed to delete the firewall rules.

[View post](https://mastodon.social/@azureshit/112404172459197344)

---

## 2024-05-06T04:35:03.362Z

Day 220. Clarifying the shit from day 217. When you disable public network access on your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL single server instance, you are no longer allowed to edit your instance's firewall rules. That includes deleting already existing firewall rules which get preserved even though you disable public network access.

[View post](https://mastodon.social/@azureshit/112392280693761688)

---

## 2024-05-03T06:35:31.182Z

Day 219. As we covered on day 191, deleting an [#Azure](https://mastodon.social/tags/Azure) Backup Vault or backup instance through Terraform results in the resource remaining in soft-deleted state even though the resource gets removed from the Terraform state. But if you also manage your backup policies in Terraform and try to subsequently delete them, the deletion will fail because the associated backup instance is in soft-deleted state, effectively breaking your Terraform operations.

[View post](https://mastodon.social/@azureshit/112375767444931888)

---

## 2024-05-02T12:39:09.751Z

Day 218. The [#Azure](https://mastodon.social/tags/Azure) Portal does not show you any networking configuration for your Service Bus in Standard Tier but only for the more expensive Premium Tier. For Standard Tier, you need to use the API or another client.

[View post](https://mastodon.social/@azureshit/112371535036322717)

---

## 2024-04-22T07:34:05.795Z

Day 217. The [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider allows you to create firewall rules for Azure Database for PostgreSQL single server. But if you then try to delete that resource through Terraform, the deletion suddenly fails because the "requested feature is not enabled".

[View post](https://mastodon.social/@azureshit/112313712364415218)

---

## 2024-04-19T08:40:02.287Z

Day 216. The [#Azure](https://mastodon.social/tags/Azure) resource provider for Azure Resource Graph only overwrites the deployment of query resources after they have already passed policy evaluation. When you have an Azure Policy that denies all global resources for legal or compliance reasons, users could simply specify any allowed region, would thereby bypass the policy and still end up with a global resource.

[View post](https://mastodon.social/@azureshit/112296984725638585)

---

## 2024-04-18T06:50:49.270Z

Day 215. While you can specify other locations when deploying [#Azure](https://mastodon.social/tags/Azure) Resource Graph queries through the API, the resource provider will simply overwrite your specified location with "global". Which of course hasn't been documented in the API documentation.

[View post](https://mastodon.social/@azureshit/112290892956732420)

---

## 2024-04-17T07:47:46.946Z

Day 214. The [#Azure](https://mastodon.social/tags/Azure) Portal will deploy Azure Resource Graph query resources always to the "global" location, not allowing you to specify any other location, even though the resource data model supports the "location" property.

[View post](https://mastodon.social/@azureshit/112285454626885584)

---

## 2024-04-16T07:45:56.320Z

Day 213. Continuing the shit from day 212, if you want your ADF SSIS-IR to use a custom DNS server for it to be able to work in a hub-and-spoke environment, you need to run some weird PowerShell scripts during Integration Runtime startup and provide these scripts in an [#Azure](https://mastodon.social/tags/Azure) Storage account.

[View post](https://mastodon.social/@azureshit/112279785025766780)

---

## 2024-04-15T12:36:38.150Z

Day 212. [#Azure](https://mastodon.social/tags/Azure) SQL Server Integration Services (SSIS) Integration Runtimes (IR) for Azure Data Factory (ADF) - ADF SSIS-IR 🤦 - do not respect the custom DNS server you configure in your VNet and instead always use the default Azure-provided DNS server.

[View post](https://mastodon.social/@azureshit/112275265824229881)

---

## 2024-04-14T21:23:27.563Z

Day 211. [#Azure](https://mastodon.social/tags/Azure) App Service per default exposes an IIS management port for Web Apps. You don't want your Web App to come with this open port? Easy, simply redeploy it until you land on an underlying server where that port has been deactivated.

[View post](https://mastodon.social/@azureshit/112271675063466567)

---

## 2024-04-12T08:32:43.760Z

Day 210. Following up on the shit from day 209, the role assignments are only uncompliant in case the resource they have been scoped to is in the "global" location. Which lets us suspect that some Azure resources can derive properties from parent resources when evaluated by an [#Azure](https://mastodon.social/tags/Azure) policy. You think they would document that behavior somewhere? Think again.

[View post](https://mastodon.social/@azureshit/112257319813717854)

---

## 2024-04-11T07:45:41.362Z

Day 209. This role assignment gets evaluated by an [#Azure](https://mastodon.social/tags/Azure) Policy and flagged as uncompliant because its location is set to "global". But hold on, role assignments don't even have a location property according to the API specifications. So how could it be uncompliant?

[View post](https://mastodon.social/@azureshit/112251472534523917)

---

## 2024-04-10T08:14:36.015Z

Day 208. Some [#Azure](https://mastodon.social/tags/Azure) resources are only supported to be deployed to some Azure regions and sometimes the API docs tell you so, but sometimes they don't and you need to guess locations.

[View post](https://mastodon.social/@azureshit/112245923905908118)

---

## 2024-04-09T07:24:01.271Z

Day 207. [#Azure](https://mastodon.social/tags/Azure) DNS is a global service and all its resources need to be deployed to the 'Global' region. But if you try to deploy a DNS zone to a different region, the Azure API tells you can simply fix this by re-registering the corresponding provider, which is just a lie.

[View post](https://mastodon.social/@azureshit/112240062710948204)

---

## 2024-04-08T08:44:20.617Z

Day 206. These orphaned [#Azure](https://mastodon.social/tags/Azure) Advsior recommendations now get flagged as non-compliant by Azure Policies because the parent resource they apply to is long gone. Good luck trying to get to 100% resource compliance.

[View post](https://mastodon.social/@azureshit/112234716241395454)

---

## 2024-04-05T09:31:24.795Z

Day 205. [#Azure](https://mastodon.social/tags/Azure) Advisor recommendation resources for some reason continue to exist for weeks when their parent resource (to which the recommendation applies to) gets deleted. Even though the Azure Advisor dashboard shows they have been updated recently.

[View post](https://mastodon.social/@azureshit/112217914395378442)

---

## 2024-04-04T08:15:46.748Z

Day 204. The multitude of different purchasing models, service tiers and compute tiers with Azure SQL database apparently even confused Microsoft's technical writers. They say the DTU-based purchasing model comes with three service tiers but then only explain two of them.

[View post](https://mastodon.social/@azureshit/112211954679359421)

---

## 2024-04-03T07:26:27.846Z

Day 203. Our development teams have encountered this problem multiple times now: An [#Azure](https://mastodon.social/tags/Azure) Kubernetes cluster being in a failed provisioning state, but Azure can't give you any reason for that and you have no hints at all regarding what might be broken.

[View post](https://mastodon.social/@azureshit/112206098454421589)

---

## 2024-04-02T08:35:57.460Z

Day 202. Instead of restoring an old key version in [#Azure](https://mastodon.social/tags/Azure) Key Vault, the only thing you can do is to enable the old version and disable the current version. But this will still label your whole key as "disabled".

[View post](https://mastodon.social/@azureshit/112200709403891819)

---

## 2024-03-30T09:32:18.861Z

Day 201. When registering features in your [#Azure](https://mastodon.social/tags/Azure) subscription, you need to re-register the corresponding provider to get the change to propagate, even when the provider has already been registered before.

[View post](https://mastodon.social/@azureshit/112183944076083601)

---

## 2024-03-29T10:04:27.964Z

Day 200. After more than one year and now 200 [#Azure](https://mastodon.social/tags/Azure) shits, what still infuriates us the most is that when you are billed through a CSP, you cannot create new subscriptions directly with Azure. The Subscriptions API is off limits to you and you also cannot easily maintain tags or aliases for existing subscriptions. Nobody in this Microsoft Cloud Solution Provider program actually cares about offering developer-friendly products. It's all about 🤑 and managers love that.

[View post](https://mastodon.social/@azureshit/112178408191448781)

---

## 2024-03-28T10:00:34.966Z

Day 199. [#Azure](https://mastodon.social/tags/Azure) Activity Log alert rules are allowed to get deployed in multiple Azure regions, but the [#Terraform](https://mastodon.social/tags/Terraform) provider does not care about any of that and always deploys them to the "Global" location.

[View post](https://mastodon.social/@azureshit/112172730610888015)

---

## 2024-03-27T06:28:16.693Z

Day 198. The only way to force your [#Azure](https://mastodon.social/tags/Azure) Application Gateway to refresh DNS lookup results is to stop and restart it, which results in a downtime of up to 20 minutes.

[View post](https://mastodon.social/@azureshit/112166233485533471)

---

## 2024-03-26T09:20:59.752Z

Day 197. In [#Azure](https://mastodon.social/tags/Azure) Key Vault, there is no way to restore an old version of a key so that it would become the current version again.

[View post](https://mastodon.social/@azureshit/112161250328432682)

---

## 2024-03-25T08:58:11.009Z

Day 196. Continuing the shit from day 195, when you want to use RBAC instead of access policies on your [#Azure](https://mastodon.social/tags/Azure) Key Vault, suddenly you can no longer configure the Application Gateway through [#Terraform](https://mastodon.social/tags/Terraform) to do so, but need to run some CLI or PowerShell commands.

[View post](https://mastodon.social/@azureshit/112155498316163220)

---

## 2024-03-25T01:08:13.567Z

Day 110. (repost) Trying to lock the immutability of an unlocked [#Azure](https://mastodon.social/tags/Azure) Backup Vault will fail with the error message "immutability is already locked cannot be disabled" if the Vault did not have immutability enabled before. You have to first set it to "Unlocked" and then to "Locked", but the error message is completely wrong.

[View post](https://mastodon.social/@azureshit/112153650368642120)

---

## 2024-03-22T13:13:40.755Z

Day 195. When you want to serve a TLS certificate from an [#Azure](https://mastodon.social/tags/Azure) Key Vault with Azure Application Gateway, you can use Terraform to instruct the App Gateway which certificate to use. But for some reason that only works when your Key Vault uses access policies instead of RBAC.

[View post](https://mastodon.social/@azureshit/112139516035034338)

---

## 2024-03-21T14:00:20.503Z

Day 194. When listing key versions of an [#Azure](https://mastodon.social/tags/Azure) Key Vault key with "az keyvault key list-versions", the key versions get sorted by their random alphanumeric IDs.

[View post](https://mastodon.social/@azureshit/112134037200399975)

---

## 2024-03-20T18:20:35.284Z

Day 193. When using an [#Azure](https://mastodon.social/tags/Azure) Storage Account as state backend for [#Terraform](https://mastodon.social/tags/Terraform), it will sometimes fail to release the state lock because the Azure API returns gibberish.

[View post](https://mastodon.social/@azureshit/112129398228891156)

---

## 2024-03-19T21:48:00.382Z

Day 192. Minor releases of the [#Azure](https://mastodon.social/tags/Azure) CLI regularly come with breaking changes, which is not how Semantic Versioning is supposed to work.

[View post](https://mastodon.social/@azureshit/112124551520434345)

---

## 2024-03-18T19:29:35.478Z

Day 191. Recently, soft delete was introduced for [#Azure](https://mastodon.social/tags/Azure) Backup and enabled by default on all newly created Backup Vaults. If you now delete such a new a Backup Vault through [#Terraform](https://mastodon.social/tags/Terraform), the vault will be preserved in soft-deleted state but completely removed from the Terraform state. Trying to recreate the vault through Terraform now fails because a vault with the same name already exists.

[View post](https://mastodon.social/@azureshit/112118344936094473)

---

## 2024-03-15T09:34:15.067Z

Day 190. Continuing the shit from day 187. The [#Azure](https://mastodon.social/tags/Azure) Activity Logs are as useless as always. And what kind of shitty operation name is "Update Create"?

[View post](https://mastodon.social/@azureshit/112099017035969778)

---

## 2024-03-14T10:05:09.754Z

Day 189. Continuing the shit from day 188, we just thought the [#Aure](https://mastodon.social/tags/Aure) Database for PostgreSQL instance got deployed, but it was nowhere to be found in the Azure Portal. And with Azure APIs all involuntarily being eventually consistent, you can't know for sure and are now once again hunting ghost resources with an unknown deployment state.

[View post](https://mastodon.social/@azureshit/112093476273347990)

---

## 2024-03-13T08:16:41.174Z

Day 188. If you thought the Gateway Timeout from day 187 resulted in the [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL instance not being deployed, you were wrong. The instance apparently got deployed but since the [#Terraform](https://mastodon.social/tags/Terraform) provider doesn't know that, recreating will fail and you now need to manually import the resource. Good luck automating your infrastructure on Azure.

[View post](https://mastodon.social/@azureshit/112087387417585585)

---

## 2024-03-12T13:06:45.224Z

Day 187. Deployment of our [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL single server through [#Terraform](https://mastodon.social/tags/Terraform) failed due to an ominous Gateway Timeout.

[View post](https://mastodon.social/@azureshit/112082865698829342)

---

## 2024-03-11T18:33:17.656Z

Day 186. There is no such thing as a small Docker image with the [#Azure](https://mastodon.social/tags/Azure) CLI. Installing just the CLI on Alpine Linux results in images of around 400MB.

[View post](https://mastodon.social/@azureshit/112078487398068027)

---

## 2024-03-08T09:12:53.637Z

Day 185. Continuing the shit with the broken backups from day 175, the Microsoft support came back to us and said that the product team changed the permissions of the psqladmin user because they considerd it to be a "security loophole", even though the documentationa advertised it as feature. This change broke our existing production backups for [#Azure](https://mastodon.social/tags/Azure) PostgreSQL single server which we set up according to their documentation. They promised to update the documentation soon.

[View post](https://mastodon.social/@azureshit/112059296882960728)

---

## 2024-03-06T08:50:22.822Z

Day 184. The API for [#Azure](https://mastodon.social/tags/Azure) Container Apps allows you to specify a name when creating an auth config, but the only valid name is "current".

[View post](https://mastodon.social/@azureshit/112047883735446456)

---

## 2024-03-05T11:58:50.663Z

Day 183. The [#Azure](https://mastodon.social/tags/Azure) documentation gives you an example on how to deploy auth configs for Azure Container Apps through Terrraform, but if you copy the example, it tells you that API version is invalid.

[View post](https://mastodon.social/@azureshit/112042962495718776)

---

## 2024-03-04T10:57:25.732Z

Day 182. A few days ago, [#Azure](https://mastodon.social/tags/Azure) accidentally introduced a breaking change in their Insights API which provides activity logs. The "EventLevel" of a log had been changed from a string to a number, thereby breaking the Azure SDK for Go and all other clients that used that functionality. After multiple reports on GitHub, it took Microsoft engineers one week to fix it.

[View post](https://mastodon.social/@azureshit/112037058689745931)

---

## 2024-03-03T16:15:23.047Z

Day 181. This [#GitHub](https://mastodon.social/tags/GitHub) issue about [#Azure](https://mastodon.social/tags/Azure) App Configuration not working correctly got closed not because the issue had been resolved, but because the customer no longer used the product.

[View post](https://mastodon.social/@azureshit/112032646630167653)

---

## 2024-03-02T14:48:14.823Z

Day 180. The [#Azure](https://mastodon.social/tags/Azure) SDK for Go sometimes fails to authenticate with environment variables and falls back to the identity of the CLI. This is really annoying, especially when you want the SDK to use a different identity than your local user by setting those variables.

[View post](https://mastodon.social/@azureshit/112026641682354150)

---

## 2024-03-01T16:16:38.431Z

Day 179. The shit from day 178 did not happen because AKS version 1.29.0 is in preview. It still is, but somehow now the deployment goes through.

[View post](https://mastodon.social/@azureshit/112021326949873218)

---

## 2024-02-28T12:46:52.474Z

Day 178. 🎂 The [#Azure](https://mastodon.social/tags/Azure) CLI shows you AKS version 1.29 as available, but you cannot create a cluster with that version through the Azure [#Terraform](https://mastodon.social/tags/Terraform) provider because "version not found". It magically worked after waiting a few days.

[View post](https://mastodon.social/@azureshit/112009177495541039)

---

## 2024-02-21T10:06:11.957Z

Day 177. The [#Azure](https://mastodon.social/tags/Azure) Firewall sometimes allows traffic while denying the same request only moments later. We suspect this is due to multiple Firewall instances caching different DNS results when evaluating whether to allow traffic to specific FQDNs.

[View post](https://mastodon.social/@azureshit/111968909521945417)

---

## 2024-02-19T20:54:11.326Z

Day 176. Essentially no useful information is available for these [#Azure](https://mastodon.social/tags/Azure) Firewall logs.

[View post](https://mastodon.social/@azureshit/111960132899318361)

---

## 2024-02-15T09:56:19.460Z

Day 175. Continuing the shit with the broken backups from day 173, the [#Azure](https://mastodon.social/tags/Azure) support told us that we need to assign additional permissions for the PostgreSQL admin user for backups to complete. We never had to do this before and their documentation even says otherwise. So this was yet again a breaking change to their product Azure rolled out without any prior notice (or even bothering to update the docs), breaking our database backups on our production environment.

[View post](https://mastodon.social/@azureshit/111934896829749040)

---

## 2024-02-14T09:55:42.608Z

Day 174. [#Azure](https://mastodon.social/tags/Azure) once again experienced degraded availability and customers are rightfully wondering why they even bother to have a status dashboard if it always fails to inform about ongoing issues.

[View post](https://mastodon.social/@azureshit/111929232104183769)

---

## 2024-02-13T09:17:26.054Z

Day 173. Continuing the shit from day 172, we contacted the [#Azure](https://mastodon.social/tags/Azure) support after a few days of troubleshooting. They told us that they received many similar support requests in the past few days and that they are investigating. Sounds like yet another broken Azure product.

[View post](https://mastodon.social/@azureshit/111923419286800577)

---

## 2024-02-12T09:06:59.757Z

Day 172. Our [#Azure](https://mastodon.social/tags/Azure) Backup Vault backups for Database for PostgreSQL single server instances haven't been working since Jan 24. They are failing with with "UserErrorMissingDBPermissions". This issue occured simultaneously on all of our environments without us rolling out any changes. Even deploying the setup from scratch does not fix it.

[View post](https://mastodon.social/@azureshit/111917715930356042)

---

## 2024-02-09T13:08:46.932Z

Day 171. The button in the [#Azure](https://mastodon.social/tags/Azure) Portal to refresh the view of system-assigned identities of an App Service app doesn't do anything.

[View post](https://mastodon.social/@azureshit/111901679742414712)

---

## 2024-02-08T14:28:13.939Z

Day 170. [#Microsoft](https://mastodon.social/tags/Microsoft) Defender for Cloud is invoking costs per [#Azure](https://mastodon.social/tags/Azure) subscription, even if there aren't any resources in your subscription.

[View post](https://mastodon.social/@azureshit/111896329842385931)

---

## 2024-02-07T11:49:40.727Z

Day 169. This example out of the [#Azure](https://mastodon.social/tags/Azure) SDK for Go shows how to write documentation if you have to but don't want to.

[View post](https://mastodon.social/@azureshit/111890044074301292)

---

## 2024-02-05T13:39:17.266Z

Day 168. Contrary to what you might expect, the [#Azure](https://mastodon.social/tags/Azure) CLI commands "az backup vault" are not getting used for the [#Azure](https://mastodon.social/tags/Azure) Backup Vault but instead for the Azure Backup Recovery Services vault which is a totally different product. For Backup Vaults, you need to use "az dataprotection backup-vault".

[View post](https://mastodon.social/@azureshit/111879150453547303)

---

## 2024-01-29T14:15:44.599Z

Day 167. Continuing the shit from day 166, while you cannot update the key vault reference in your [#Azure](https://mastodon.social/tags/Azure) Backup Vault backup instance, the API will happily tell you that it accepted the change and then proceeds to return the unchanged data. This results in the Azure Terraform provider being stuck in an endless loop where it tries to update the secret ID over and over again.

[View post](https://mastodon.social/@azureshit/111839657629829892)

---

## 2024-01-26T08:38:27.497Z

Day 166. When you use an [#Azure](https://mastodon.social/tags/Azure) Backup Vault to backup your Azure Database for PostgreSQL instance and then move the connection string for the backup instance to another key vault, there is no way to update the backup instance to let it use the new connection string. You would need to replace the instance, which you can't do in case your backup vault is immutable.

[View post](https://mastodon.social/@azureshit/111821344436804634)

---

## 2024-01-25T13:36:35.625Z

Day 165. The maintainers of the [#Azure](https://mastodon.social/tags/Azure) SDK for Golang seem to live in an entirely different timezone because their 5.5.0 release date has been off by two days. Maybe that somehow explains why ID tokens that get issued are sometimes not yet valid (see shit from day 119).

[View post](https://mastodon.social/@azureshit/111816854443535947)

---

## 2024-01-24T08:54:15.358Z

Day 164. The field "application\_id" in the "azuread\_service\_principal" data source in the [#Azure](https://mastodon.social/tags/Azure) Terraform Provider is deprecated, but the depraction reason in VS Code is simply the description of the field.

[View post](https://mastodon.social/@azureshit/111810081938097136)

---

## 2024-01-23T10:54:02.964Z

Day 163. The shit from day 162 didn't actually take more than 15 minutes. Instead, the Terraform provider just didn't recognize that the deletion of the database server failed. And of course the activity logs don't show any useful information besides that the deletion failed with state "Failed".

[View post](https://mastodon.social/@azureshit/111804890674828593)

---

## 2024-01-22T09:15:07.553Z

Day 162. It can take over 15 minutes to delete an [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL server through the Azure Terraform provider.

[View post](https://mastodon.social/@azureshit/111798839381186639)

---

## 2024-01-19T13:59:37.040Z

Day 161. [#Azure](https://mastodon.social/tags/Azure) Load Balancer load balancing rules have a property called "disableOutboundSnat" which configures whether response traffic from the backend pool is allowed to return to the Internet without you needing to declare dedicated outbound rules. However, in case you want to have special outbound rules which are unrelated to inbound traffic, you need to disable this behavior for every single inbound rule.

[View post](https://mastodon.social/@azureshit/111782971115732070)

---

## 2024-01-18T08:27:22.574Z

Day 160. Navigating the [#Azure](https://mastodon.social/tags/Azure) Activity Logs in the portal is an Excel-style nightmare.

[View post](https://mastodon.social/@azureshit/111776002380280266)

---

## 2024-01-17T09:00:42.201Z

Day 159. When deleting an [#Azure](https://mastodon.social/tags/Azure) Backup Vault backup instance, Microsoft requires you to provide a reason for deleting the instance.

[View post](https://mastodon.social/@azureshit/111770471117317686)

---

## 2024-01-16T09:46:25.197Z

Day 158. When trying to send sample [#Microsoft](https://mastodon.social/tags/Microsoft) Defender for Cloud alerts for your [#Azure](https://mastodon.social/tags/Azure) subscriptions, it won't give you any failure reasons if it fails. You have to investigate your browser's network traffic to see the API response, for example error 403.

[View post](https://mastodon.social/@azureshit/111764988572130028)

---

## 2024-01-11T12:33:12.015Z

Day 157. Adding a subnet to your [#Azure](https://mastodon.social/tags/Azure) Storage Account's virtual network allow list and then trying to deploy that Storage account through Terraform will fail in case the referenced subnet does not have Service Endpoints configured. But the error message that the API then throws makes no sense at all and is more than misleading: "The storage account \*\*\*\*\* was not found".

[View post](https://mastodon.social/@azureshit/111737332826869975)

---

## 2024-01-10T09:50:38.079Z

Day 156. The [#Azure](https://mastodon.social/tags/Azure) Terraform provider needs to replace the database for Azure PostgreSQL flexible server just because somehow the leading "/" in the ID of the referenced server got removed - even though it is still the same server. While this behavior of the Terraform provider might be understanable, different Azure clients and APIs always implementing different appraoches when it comes to leading or trailing slahes and and even lower and upper case identfiers is shit.

[View post](https://mastodon.social/@azureshit/111731031281768905)

---

## 2024-01-08T10:24:27.392Z

Day 155. Specifying the shit from day 16, when elevating to a security group with Azure AD / Entra ID Privileged Identity Management (what a shitty name), the Azure Portal will only retrieve your new permissions in the browser tab you used to elevate yourself. All other open browser tabs will still have the old permissions and you need to sign out and sign in again for them to populate.

[View post](https://mastodon.social/@azureshit/111719839654888194)

---

## 2024-01-05T12:33:18.805Z

Day 154. Deployment of [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server fails because the "selected subscription is disabled", but they do not provide any explanation what that means.

[View post](https://mastodon.social/@azureshit/111703359409430596)

---

## 2024-01-04T11:41:21.951Z

Day 153. When deploying [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server resources through the Azure Terraform provider, for some unknown reason the deployment will fail with "Internal Server Error" and "OperationFailed" statuses.

[View post](https://mastodon.social/@azureshit/111697492832908092)

---

## 2024-01-03T12:58:00.599Z

Day 152. The [#Azure](https://mastodon.social/tags/Azure) Marketplace has two SKUs availabke for HAProxy 2.8 Enterprise: "2\_8r1\_1" and "2\_8\_r1\_1", but the latter one seems to be a typo which they just didn't bother to remove, because there are no image versions available for it.

[View post](https://mastodon.social/@azureshit/111692131899591146)

---

## 2024-01-02T12:31:58.684Z

Day 151. Continuing the shit from day 150, the link to the docs you should view for more details on why your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server suddenly does not support Private Endpoints redirects to a no longer existing GitHub repository on the private profile of a Microsoft employee.

[View post](https://mastodon.social/@azureshit/111686367227474586)

---

## 2023-12-15T11:59:24.502Z

Day 150. Continuing the shit from day 149, when you then guess the correct subresource identifier targeted by Private Endpoints for [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server instances, the Azure API will tell you that the server you just created does not support Private Endpoints.

[View post](https://mastodon.social/@azureshit/111584317570872144)

---

## 2023-12-14T10:50:54.033Z

Day 149. According to the [#Azure](https://mastodon.social/tags/Azure) docs, Azure Database for PostgreSQL flexible server supports Private Endpoints in preview, but the Private Link documentation does not list the service's subresource identifier you need to make Azure's DNS-at-scale concept work.

[View post](https://mastodon.social/@azureshit/111578385876789125)

---

## 2023-12-13T11:01:19.252Z

Day 148. Microsoft [#Azure](https://mastodon.social/tags/Azure) AD / Microsoft Entra ID Privileged Identity Management (great name, btw) is unavailable right now, leaving customers unable to elevate to roles with elevated permissions, for example to perform production deployments.

[View post](https://mastodon.social/@azureshit/111572764540908287)

---

## 2023-12-12T11:31:11.200Z

Day 147. [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL single server instances have been deprecated and - according to the docs - can no longer get deployed through the Azure Portal since November 30, 2023. Except you totally still can deploy them through the Azure Portal.

[View post](https://mastodon.social/@azureshit/111567219662478261)

---

## 2023-12-11T08:42:49.422Z

Day 146. The only way to configure IP allowlists for Azure-managed Databricks workspaces is through the proprietary API of the Databricks control plane. The [#Azure](https://mastodon.social/tags/Azure) resource itself does not support IP allowlists, which makes it impossible to maintain them through the Azure Resource Manager or to evaluate them in any way through Azure policies.

[View post](https://mastodon.social/@azureshit/111560895326112923)

---

## 2023-12-08T10:55:20.487Z

Day 145. If you need any more proof that the [#Azure](https://mastodon.social/tags/Azure) REST API is shit: Even the Azure Terraform provider has to work around the API returning inconsistent and outdated information.

[View post](https://mastodon.social/@azureshit/111544429476815851)

---

## 2023-12-07T08:56:26.175Z

Day 144. When you deploy an [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server through the Azure Portal and let it create a vnet with delegated subnet for you, these resources will be created by some unknown "Meru19 First Party App" and there exists hardly any documentation on it.

[View post](https://mastodon.social/@azureshit/111538299612140202)

---

## 2023-12-06T09:53:02.003Z

Day 143. If you deploy an [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL flexible server with public access, there is no way to make it private afterwards.

[View post](https://mastodon.social/@azureshit/111532859850767305)

---

## 2023-12-05T09:12:43.961Z

Day 142. The [#Azure](https://mastodon.social/tags/Azure) CLI is full of random errors that occur sporadically and if you get to fix them, you never fully understood what just happend. In this case the CLI extensions are not compatible with the CLI version you have installed, but if you check the version, it's a totally different one than the Azure SDK claimed.

[View post](https://mastodon.social/@azureshit/111527039071572229)

---

## 2023-12-04T09:05:43.533Z

Day 141. When using [#Azure](https://mastodon.social/tags/Azure) Firewall, not only are you limited to the shit from day 140, but each rule collection group can have at most 2 MB of rules. You might wonder that this is a weird unit to measure firewall rules. How do you even know how large your rule collection group currently is? Easy, according to the Microsoft support, just download the JSON representation of the firewall policy and check it for yourself.

[View post](https://mastodon.social/@azureshit/111521349203726972)

---

## 2023-12-02T11:26:12.931Z

Day 140. When using the [#Azure](https://mastodon.social/tags/Azure) Firewall, you can have at most 60 rule collections groups, which is once again another completely arbitrary limitation Microsoft does not explain and which makes it more difficult to use this product in large-scale environments.

[View post](https://mastodon.social/@azureshit/111510577016199252)

---

## 2023-11-30T08:20:34.709Z

Day 139. To work around the broken built-in Azure policies from day 138, some customers turn to Microsoft support which then confirms that the policy is not working as intended and magically overrides the policy compliance for them. However, the underlying problem remains unresolved and existing GitHub issues get closed.

[View post](https://mastodon.social/@azureshit/111498522441062718)

---

## 2023-11-29T10:50:21.150Z

Day 138. As a direct consequence of the shit from day 137, the ISO27001 policy initiative uses built-in policies that are based on outdated resource data models and don't work anymore. If you use these resources (for example Azure Key Vault), you will never be fully compliant with ISO27001 - at least according to Azure.

[View post](https://mastodon.social/@azureshit/111493449066016139)

---

## 2023-11-28T08:28:13.824Z

Day 137. When [#Azure](https://mastodon.social/tags/Azure) Policies audit existing resources, they always interpret the resource in the data model of the latest API version. Because there is no proper versioning of policies, this means that the release of a new API version might instantly break existing policies, even the ones that are built-in and maintained by Microsoft, if they are not updated to the new data model fast enough.

[View post](https://mastodon.social/@azureshit/111487227904732133)

---

## 2023-11-27T12:21:57.457Z

Day 136. The shit from day 106 happens because the "ipSecurityRestrictionsDefaultAction" property in [#Azure](https://mastodon.social/tags/Azure) App Service Web Apps is actually a property of a child resource and does not get properly represented when querying the parent resource. You need to explicitly perform a GET request on the child resource if you want to see any other values than "null".

[View post](https://mastodon.social/@azureshit/111482484651049480)

---

## 2023-11-22T09:02:38.943Z

Day 135. In the [#Azure](https://mastodon.social/tags/Azure) Portal, you can see until when Policy exemptions are valid, but you cannot see when they have been created or for how long they already have been valid. How is this not useful information?

[View post](https://mastodon.social/@azureshit/111453389385676013)

---

## 2023-11-21T14:55:35.438Z

Day 134. Another example for the shit from day 133. Using a "modify" effect policy on a field with the "[\*]" array alias, the Azure policy is (according to the docs) supposed to remove all existing values in the array and to append all your values. But that does not work with the "Microsoft.Network/virtualNetworks/dhcpOptions.dnsServers[\*]" alias. Instead the values only get appended in case they don't already exist in the array, leaving all existing values where they are.

[View post](https://mastodon.social/@azureshit/111449114898447610)

---

## 2023-11-17T09:49:43.429Z

Day 133. It's not easy to understand the "[\*]" alias for arrays in [#Azure](https://mastodon.social/tags/Azure) policies. Especially because the examples in the documentation dot not apply to all use cases.  
For example, Azure instructs you to use the "modify" effect without the "[\*]" array alias to append all your values to the existing array, but the alias "Microsoft.Network/virtualNetworks/dhcpOptions.dnsServers" is not even modifiable, meaning you are not allowed to use it in a "modify" effect policy.

[View post](https://mastodon.social/@azureshit/111425262939034500)

---

## 2023-11-13T12:21:10.993Z

Day 132. When providing invalid service principal credentials to the [#Azure](https://mastodon.social/tags/Azure) Terrform Provider and running terraform apply, [#Terraform](https://mastodon.social/tags/Terraform) will simply freeze and not do anything instead of giving you a helpful error message.

[View post](https://mastodon.social/@azureshit/111403209260216884)

---

## 2023-11-10T11:24:56.785Z

Day 131. When performing updates on [#Azure](https://mastodon.social/tags/Azure) Vnet subnets, the produced activity logs are not able to show what actually happened, because "change history is not applicable to this type of activity log". Isn't that the whole point of activity logs?

[View post](https://mastodon.social/@azureshit/111386001197163863)

---

## 2023-11-06T09:47:03.827Z

Day 130. When deploying an [#Azure](https://mastodon.social/tags/Azure) Database for MariaDB instance through the [#Azure](https://mastodon.social/tags/Azure) Portal, you cannot even configure it to be private. The "publicNetworkAccess" property can only be changed after the instance has already been deployed.

[View post](https://mastodon.social/@azureshit/111362967065324990)

---

## 2023-11-03T08:41:02.053Z

Day 129. DNS over UDP packets are only allowed to be larger than 512 bytes when using eDNS0, but [#Azure](https://mastodon.social/tags/Azure) DNS does not care about that.

[View post](https://mastodon.social/@azureshit/111345720495268518)

---

## 2023-11-02T15:57:54.638Z

Day 128. And because it's not bad enought already, [#Azure](https://mastodon.social/tags/Azure) Cache for Redis is not the only resource implementing the shitty firewall rules from day 126 which make it impossible to get evaluated by an Azure Policy. Both Azure Database for MariaDB and Azure SQL Database implement the exact same data model.

It's so Azure to have consistency only for shit.

[View post](https://mastodon.social/@azureshit/111341776051849250)

---

## 2023-10-31T08:41:31.000Z

Day 127. [#Azure](https://mastodon.social/tags/Azure) App Service for some reason instructs OpenTelemetry clients running in web apps to not sample and collect trace data, only for the Azure Application Insights client (which is based on OpenTelemetry) to go ahead and completely ignore this instruction. You'll need to override the header set by App Service for your own OpenTelemetry client to work properly.

[View post](https://mastodon.social/@azureshit/111328735461059973)

---

## 2023-10-30T08:41:10.322Z

Day 126. [#Azure](https://mastodon.social/tags/Azure) Cache for Redis firewall rules get represented by stand-alone child resources called "Microsoft.Cache/Redis/firewallRules". There is no way to evaluate these child resources in an Azure policy for "Microsoft.Cache/Redis" resources which makes it impossible to enforce that public Redis instances always have an IP allowlist configured.

[View post](https://mastodon.social/@azureshit/111323071795582405)

---

## 2023-10-27T08:51:42.367Z

Day 125. If you want to deploy an [#Azure](https://mastodon.social/tags/Azure) Cache for Redis instance to the public Internet with an IP address allowlist, you can only add firewall rules in the Azure Portal after you have already deployed the resource.

[View post](https://mastodon.social/@azureshit/111306126285975724)

---

## 2023-10-26T08:03:29.456Z

Day 124. This is the same [#Azure](https://mastodon.social/tags/Azure) resource, being both compliant and uncompliant at the same time. But somehow it also isn't.

[View post](https://mastodon.social/@azureshit/111300274385856114)

---

## 2023-10-25T06:16:51.052Z

Day 123. When performing API requests to the [#Azure](https://mastodon.social/tags/Azure) Management API to instruct a Vnet to use the Azure-default DNS server, the Azure Portal posts "dnsServers: null" while the [#Terraform](https://mastodon.social/tags/Terraform) client posts "dnsServers: []". Logically it's the same thing, but if you try to validate deployments through Azure Policy, you now need to check multiple constellations.

[View post](https://mastodon.social/@azureshit/111294192749569903)

---

## 2023-10-24T13:27:55.293Z

Day 122. You can't configure to back up your [#Azure](https://mastodon.social/tags/Azure) Database for PostgreSQL server to multiple Backup vaults. This makes it impossible to gradually transition from a locked vault to one with different configuration, for example with different redundancy settings.

[View post](https://mastodon.social/@azureshit/111290225477146220)

---

## 2023-10-23T17:43:21.394Z

Day 121. Yet another example of resource name consistency in [#Azure](https://mastodon.social/tags/Azure). Today: Azure Policy aliases for Azure Cache for Redis.

[View post](https://mastodon.social/@azureshit/111285567576937567)

---

## 2023-10-19T11:31:40.689Z

Day 120. As seen on day 117, you can delete Storage Account backup instances in locked immutable [#Azure](https://mastodon.social/tags/Azure) Backup Vaults and restore them in a different vault, but you can't do the same for Azure Database for PostgreSQL server backup instances. Apparently each Backup vault data source behaves completely differently when it comes to retention behavior.

[View post](https://mastodon.social/@azureshit/111261456838664705)

---

## 2023-10-17T09:38:35.030Z

Day 119. When being logged in to the [#Azure](https://mastodon.social/tags/Azure) CLI and trying to use its credentials for an Azure SDK, Azure will frequently tell you that "The ID token is not yet valid. Make sure your computer's time and time zone are both correct". There exist multiple open GitHub issues for this and Microsoft has yet failed to explain how this can happen so regularly for seemingly no reason. Sometimes logging out and in again works, sometimes not. Sometimes restarting your shell works, sometimes not.

[View post](https://mastodon.social/@azureshit/111249687507619954)

---

## 2023-09-22T15:12:43.318Z

Day 118. On their [#Azure](https://mastodon.social/tags/Azure) pricing website, Microsoft has put a (likely buggy) transparent pop-up that you cannot close and that prevents you from copying text.

[View post](https://mastodon.social/@azureshit/111109443634974061)

---

## 2023-09-20T12:42:18.807Z

Day 117. Contrary to the information in the [#Azure](https://mastodon.social/tags/Azure) documentation, you can still delete Azure Backup Vault backup instances for Azure Storage Blobs when the Backup Vault has an enabled and locked immutability policy. However, the backed up data magically gets preserved and restored if you re-create the backup instance.

[View post](https://mastodon.social/@azureshit/111097527586459743)

---

## 2023-09-11T15:00:41.409Z

Day 116. When creating an [#Azure](https://mastodon.social/tags/Azure) service principal password through [#Terraform](https://mastodon.social/tags/Terraform), the corresponding client credentials do not show up in the Azure Portal. You will need to use the Azure CLI to find them.

[View post](https://mastodon.social/@azureshit/111047110910488260)

---

## 2023-08-27T18:17:45.664Z

Day 115. When querying for [#Azure](https://mastodon.social/tags/Azure) Firewall Logs in Azure Monitor, you can filter based on the response duration of a request, but for some reason it's a string, so you can't compare it against numbers.

[View post](https://mastodon.social/@azureshit/110962951170432897)

---

## 2023-08-25T12:30:22.665Z

Day 114. The [#Azure](https://mastodon.social/tags/Azure) Storage Account Resource Provider will sometimes "validate tagged traffic consumers" and according entries will appear in the activity log. However, they don't tell you what this means, what happens or even what a "tagged traffic consumer" is. There is no documentation on such an Azure resource.

[View post](https://mastodon.social/@azureshit/110950260581644677)

---

## 2023-08-23T15:59:48.653Z

Day 113. Enabling DDoS IP protection for an [#Azure](https://mastodon.social/tags/Azure) Public IP address fails because the "ajaxExtended call" failed.

[View post](https://mastodon.social/@azureshit/110939759486461158)

---

## 2023-08-15T10:31:36.391Z

Day 112. Creating an [#Azure](https://mastodon.social/tags/Azure) Backup Instance for a PostgreSQL database through [#Terraform](https://mastodon.social/tags/Terraform) will regularly fail with the error "unexpected state: ProtectionError". However, the Backup Instance got created in Azure. Trying to run Terraform again will now fail because a resource with the same ID already exists and needs to get imported into the state. Good luck automating your Azure infrastructure.

[View post](https://mastodon.social/@azureshit/110893170451410359)

---

## 2023-08-11T07:07:18.782Z

Day 111. Great news, to pass Azure certifications you only need to answer "passPercent" of the questions right.

[View post](https://mastodon.social/@azureshit/110869717895290301)

---

## 2023-08-03T06:57:00.876Z

Day 109. These tooltips in the [#Azure](https://mastodon.social/tags/Azure) Backup vault creation wizward are just great.

[View post](https://mastodon.social/@azureshit/110824378916351594)

---

## 2023-08-02T10:10:55.694Z

Day 108. When you make requests against the [#Azure](https://mastodon.social/tags/Azure) Management API to create / update resource and leave out optional fields which have default values, the evaluation framework of Azure policies does not evaluate the defaults for these fields because they are not present in the request body. This makes it really hard to check for certain resource constellations and allows clients to bypass vulnerable policies.

[View post](https://mastodon.social/@azureshit/110819479105765997)

---

## 2023-08-01T16:26:51.392Z

Day 107. When initially creating a Service Bus Namespace, [#Azure](https://mastodon.social/tags/Azure) clients will only create the Service Bus resource and no Network Rule Set, which only gets created by the Azure Resource Manager after the API request already passed the policy evaluations. This makes it impossible to validate the networking rules for newly created Service Bus resources and is the reason Microsoft's own built-in policies are failing to deny public Service Bus resources - as we covered on day 94.

[View post](https://mastodon.social/@azureshit/110815295005620981)

---

## 2023-07-31T08:36:12.304Z

Day 106. Updating an [#Azure](https://mastodon.social/tags/Azure) App Service Web App's firewall default behavior according to the Azure CLI documentation results in the property being set to "null".

[View post](https://mastodon.social/@azureshit/110807782017508007)

---

## 2023-07-28T07:23:06.632Z

Day 105. Back with another installment of: Each service has their own reason why "0.0.0.0/0" is not a valid CIDR range in an IP allowlist. Today: [#Azure](https://mastodon.social/tags/Azure) Container Registry.

[View post](https://mastodon.social/@azureshit/110790507667757051)

---

## 2023-07-27T09:49:28.079Z

Day 104. [#Azure](https://mastodon.social/tags/Azure) App Service Web Apps have a property called "ipSecurityRestrictionsDefaultAction" which gets used by the Azure Portal in its API requests to set the default behavior in case no access rule matches, but this property is not documented in any API specification.

[View post](https://mastodon.social/@azureshit/110785420858056721)

---

## 2023-07-26T06:55:11.684Z

Day 103. Deleting an [#Azure](https://mastodon.social/tags/Azure) Load Balancer fails with HTTP status code "undefined".

[View post](https://mastodon.social/@azureshit/110779073277411604)

---

## 2023-07-25T07:40:44.331Z

Day 102. Trying to deploy an [#Azure](https://mastodon.social/tags/Azure) App Service Web App with enabled Zone Redundancy in West Europe fails with Azure saying that the requested feauture is not available in this region, even though the docs are stating that it is available.

[View post](https://mastodon.social/@azureshit/110773590048725462)

---

## 2023-07-24T08:26:38.749Z

Day 101. Adding to the shit from day 98, [#Azure](https://mastodon.social/tags/Azure) Key Vaults seem to have found yet another reason why "0.0.0.0/0" is not a valid CIDR range in an IP allowlist.

[View post](https://mastodon.social/@azureshit/110768108256579093)

---

## 2023-07-21T08:02:03.287Z

Day 100. To celebrate this special day, we wanted to write something nice about [#Azure](https://mastodon.social/tags/Azure) and asked around what engineers really like about it. So far we've got nothing. Even our Microsoft Certified Azure Solutions Architect Experts had no answers.

If you really like something about Azure, feel free to drop it in a comment.

[View post](https://mastodon.social/@azureshit/110751024629934958)

---

## 2023-07-20T00:57:43.151Z

Day 99. This [#Azure](https://mastodon.social/tags/Azure) App Service Web App is preconfigured to allow public network access, but once you toggle that in the Azure Portal, there is no way to switch it back.

[View post](https://mastodon.social/@azureshit/110743693764136791)

---

## 2023-07-19T05:57:34.845Z

Day 98. For [#Azure](https://mastodon.social/tags/Azure) Storage Accounts, "0.0.0.0/0" is a valid CIDR range for the IP allowlist, but it is not for Service Bus Namespaces. Apparently each service implements this validation on their own.

[View post](https://mastodon.social/@azureshit/110739210557202155)

---

## 2023-07-18T07:13:05.551Z

Day 97. Apparently this [#Azure](https://mastodon.social/tags/Azure) Service Bus Namespace does not have any networking configuration at all. Or it's yet another bug in the Azure Portal. No one can say for sure.

[View post](https://mastodon.social/@azureshit/110733845171314706)

---

## 2023-07-17T08:09:59.745Z

Day 96. While the data model and API and CLI documentation indicate that an [#Azure](https://mastodon.social/tags/Azure) Service Bus can have multiple Network Rule Sets, you are actually only allowed to create a Rule Set with the name "default", which the documentation does not mention anywhere. Anyway, multiple Rule Sets would have been weird though, because the Azure Portal is limited to showing you one Rule Set.

[View post](https://mastodon.social/@azureshit/110728406613509533)

---

## 2023-07-16T12:48:27.555Z

Day 95. Trying to create a Service Bus Network Rule set through the [#Azure](https://mastodon.social/tags/Azure) CLI. Argument missing and at the same time not supported. The documentation is just as unhelpful as always. And what does "??" even mean?

[View post](https://mastodon.social/@azureshit/110723839265534003)

---

## 2023-07-14T16:44:57.992Z

Day 94. Remember the broken [#Azure](https://mastodon.social/tags/Azure) built-in policy from day 8? After over 8 months of looking into the issue, Azure engineers came to the conclusion that their own policy does not work due to limiations in their policy evaluation framework and that there is no way to fix it.

[View post](https://mastodon.social/@azureshit/110713444629646031)

---

## 2023-07-12T08:55:21.032Z

Day 93. Not [#Azure](https://mastodon.social/tags/Azure), but another product from the suite of hell: [#Bing](https://mastodon.social/tags/Bing) isn't even able to properly align text in search results.

[View post](https://mastodon.social/@azureshit/110700273402075715)

---

## 2023-07-11T06:51:46.882Z

Day 92. Even worse than the shit from day 91, when creating a Private Endpoint in a subnet, the [#Azure](https://mastodon.social/tags/Azure) Portal will overwrite Private Endpoint Network Policies with "false" on that subnet, disregarding any previous configuration. Doing this results in all the /32 routes of Private Endpoints becoming active again which will potentially break your network connectivity.  
This is just bad implementation and not a requirement, because you can manually enable the Network Policies again afterwards.

[View post](https://mastodon.social/@azureshit/110694125199646280)

---

## 2023-07-10T06:09:56.957Z

Day 91. Enabling Private Endpoint Network Policies on subnets is not supported in the [#Azure](https://mastodon.social/tags/Azure) Portal, therefore you cannot use it to create subnets if you have an Azure policy denying subnets where they are not enabled.

[View post](https://mastodon.social/@azureshit/110688298398708693)

---

## 2023-07-08T11:37:33.542Z

Day 90. When you are using an [#Azure](https://mastodon.social/tags/Azure) Firewall as central routing component in a Hub & Spoke network topology, the shit from day 88 will break Private Endpoint network connectivity between directly peered networks and you have to enable SNAT on your Firewall to ensure symetric routing.

[View post](https://mastodon.social/@azureshit/110678261991563532)

---

## 2023-07-07T08:21:06.235Z

Day 89. Private Endpoint Network Policies is a feature for your [#Azure](https://mastodon.social/tags/Azure) subnets for invalidating the system-generated /32 routes that exist per Private Endpoint in the vnet and all peered vnets, which would normally instruct traffic to the Private Endpoint to bypass all NVAs. The docs say that this feature is disabled per default, but the Azure [#Terraform](https://mastodon.social/tags/Terraform) provider enables it per default on all subnets.

[View post](https://mastodon.social/@azureshit/110671827188398749)

---

## 2023-07-05T22:09:37.402Z

Day 88. Response traffic of [#Azure](https://mastodon.social/tags/Azure) Private Endpoints always tries to directly reach the traffic source, completely ignoring any User Defined Routes and bypassing any Network Virtual Appliance, such as your Azure Firewall.

[View post](https://mastodon.social/@azureshit/110663760438523139)

---

## 2023-07-03T08:40:08.519Z

Day 87. [#Azure](https://mastodon.social/tags/Azure) made changes to their AKS creation validation, no longer allowing clusters to have Public Network Access disabled when using User Defined Routing for egress traffic, which was previously possible. Clusters in this constellation are now considered invalid and cannot get upgraded anymore. Fixing the Public Network Access setting through the Azure [#Terraform](https://mastodon.social/tags/Terraform) provider will require the whole cluster to be recreated - resulting in downtime.

[View post](https://mastodon.social/@azureshit/110649252806522102)

---

## 2023-06-30T07:54:12.671Z

Day 86. Not [#Azure](https://mastodon.social/tags/Azure), but related to the tech stack of hell. The web app of [#Teams](https://mastodon.social/tags/Teams) quite often freezes at startup and leaves you with a completely white screen. You need to wipe cookies and browser cache for the app to work again.

[View post](https://mastodon.social/@azureshit/110632085269161086)

---

## 2023-06-29T07:23:13.452Z

Day 85. The shit from day 84 only happens when using the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider. When deploying an API Management instance in Premium SKU through the Azure Portal, Azure will still manage the Public IP address for you. This different behavior results in not being able to import already existing API Management instances into your Terraform state, because there is no Public IP address you manage and could import to satisfy the dependency to an azurerm\_public\_ip resource.

[View post](https://mastodon.social/@azureshit/110626301113103907)

---

## 2023-06-28T07:40:34.007Z

Day 84. We learned on day 82 that [#Azure](https://mastodon.social/tags/Azure) API Management instances always have a Public IP address. Normally, Azure creates and manages that IP address for you. But when deploying an API Management instance in Premium SKU in multiple availability zones with the Azure Terraform provider, you suddenly need to create the Public IP address yourself and reference it in the APIM resource. There has been an open Github issue about this since May 2022 and Microsoft yet has to come up with an explanation.

[View post](https://mastodon.social/@azureshit/110620706996463384)

---

## 2023-06-27T08:13:42.709Z

Day 83. Refreshing the state of a Public DNS Zone with the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider sometimes randomly fails with an error 503.

[View post](https://mastodon.social/@azureshit/110615175017624937)

---

## 2023-06-26T07:39:01.222Z

Day 82. For [#Azure](https://mastodon.social/tags/Azure) API Management, the difference between External and Internal vnet mode is that in External mode, you use a Public IP to perform requests to your API Management instance while it is deployed in your vnet. In Internal mode, you can no longer use a Public IP address, however, your instance will still have a Public IP address to communicate with ARM. It just does not listen to the requests you make on that Public IP.

[View post](https://mastodon.social/@azureshit/110609376295065643)

---

## 2023-06-22T06:50:07.369Z

Day 81. You could work around the shit from day 80 by assigning the [#Azure](https://mastodon.social/tags/Azure) Virtual Machine Scale Set its own Load Balancer health probe. But that does not work unless the health probe has at least one associated load balancing rule, otherwise it gets considered inactive.

[View post](https://mastodon.social/@azureshit/110586534780346108)

---

## 2023-06-21T09:28:27.642Z

Day 80. With [#Azure](https://mastodon.social/tags/Azure) Load Balancer, you cannot remove load balancing rules from an associated health probe, if that health probe is also used by a Virtual Machine Scale Set. This is because the Scale Set will block any modifications to the health probe, except adding new rules. Removing rules requires you to temporarily remove the health probe from the Scale Set or to destroy and recreate the Scale Set.

[View post](https://mastodon.social/@azureshit/110581495079699669)

---

## 2023-06-20T06:49:23.916Z

Day 79. [#Azure](https://mastodon.social/tags/Azure) Virtual Machine Scale Sets will for some reason use health probes of an Azure Load Balancer for application-level health checks. However, the Load Balancer is a completely separate resource and this creates really annoying resource dependencies, because the Load Balancer also uses the Scale Set as backend. What a weird concept.

[View post](https://mastodon.social/@azureshit/110575207311820694)

---

## 2023-06-19T05:57:09.826Z

Day 78. Annoying popups like this are what makes using Microsoft products such a shitty experience.

[View post](https://mastodon.social/@azureshit/110569339605813495)

---

## 2023-06-16T08:55:40.700Z

Day 77. Placing a management lock on an [#Azure](https://mastodon.social/tags/Azure) Container Registry that prevents it from getting deleted also prevents removal and replacement of associated Private Endpoints, even though they are a separate resource. The data representation of the Container Registry likely has a reference to the Private Endpoint and deletion of that reference is not allowed too. By the way, great error message.

[View post](https://mastodon.social/@azureshit/110553054622353054)

---

## 2023-06-15T07:03:49.152Z

Day 76. When accessing an [#Azure](https://mastodon.social/tags/Azure) Storage Account from a VM within the same region, the VM will always use its Private IP for requests, regardless of Public IPs, NAT Gateways or the lack of Private Endpoints or Service Endpoints. This means that you can only add Azure VMs to your Storage Account networking allow list by creating an approved Service Endpoint connection to the VM's vnet, even if that VM belongs to an entirely different Azure customer.

[View post](https://mastodon.social/@azureshit/110546952463836324)

---

## 2023-06-14T17:20:33.690Z

Day 75. Per default, Log Analytic Workspace logs in the [#Azure](https://mastodon.social/tags/Azure) Portal are ordered by... nothing that would make sense apparently. You have to click on the "TimeGenerated" row first to get them ordered by their timestamp.

[View post](https://mastodon.social/@azureshit/110543715282940077)

---

## 2023-06-13T11:27:37.571Z

Day 74. Creating management group associations for subscriptions with the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider sometimes fails because it "failed to add subscription to management group". Thanks, Azure.

[View post](https://mastodon.social/@azureshit/110536665174275009)

---

## 2023-06-12T12:14:02.126Z

Day 73. With the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) Provider, you can create two identical "azurerm\_resource\_group" resources with the same name. Only one resource group will be created in Azure, but now you have two Terraform resources managing the same remote resource.

[View post](https://mastodon.social/@azureshit/110531185352120518)

---

## 2023-06-07T07:33:30.087Z

Day 72. Creation of an [#Azure](https://mastodon.social/tags/Azure) Firewall rule failed with "Error: error". However, the rule still got created.

[View post](https://mastodon.social/@azureshit/110501770696040756)

---

## 2023-06-06T13:11:38.166Z

Day 71. And if you finally got the shit from day 70 to work, it will create the security contact but return an error.

[View post](https://mastodon.social/@azureshit/110497437985341650)

---

## 2023-06-05T09:03:16.282Z

Day 70. Not only does the auto-generated [#Azure](https://mastodon.social/tags/Azure) CLI documentation wrongly tell you that the "alert-notifications" attribute is optional in the "az security contact create" command, it does not even tell you what values are supported. How can you call this documentation?

[View post](https://mastodon.social/@azureshit/110490799064812070)

---

## 2023-06-02T08:04:34.634Z

Day 69. Still haven't given up using [#Azure](https://mastodon.social/tags/Azure) with [#Terraform](https://mastodon.social/tags/Terraform)? To work around the problem from day 66, you would need to deploy the API Management service through a Terraform resource and then use a null-resource with a local-exec provisioner that invokes the Azure CLI to update the API Management service to disable public network access after you created the Private Endpoint. And don't forget to instruct Terraform to ignore lifecycle changes. Good luck automating your infrastructure on Azure.

[View post](https://mastodon.social/@azureshit/110473581338957477)

---

## 2023-06-01T10:59:49.719Z

Day 68. When creating a security contact through the [#Azure](https://mastodon.social/tags/Azure) REST API, it tells you that the only supported name is "default". But if you name it "default" and look up the created security contact through the CLI, you will see that its resource name suddenly is something completely different. You can even create multiple security contacts by performing multiple PUT requests on the same resource ID.

[View post](https://mastodon.social/@azureshit/110468608144620309)

---

## 2023-05-31T09:44:20.160Z

Day 67. For newly created or recently moved [#Azure](https://mastodon.social/tags/Azure) Key Vaults, some Azure clients can sometimes fail to look up resource IDs while other Azure clients work fine. This can happen randomly even hours after provisioning and is apparently due to slow propagation of Azure services across regions. There exist several GitHub issues about this, but the Azure support teams concluded that there is nothing they can do about that.

[View post](https://mastodon.social/@azureshit/110462648985633726)

---

## 2023-05-30T08:39:29.679Z

Day 66. Remember the broken error message from day 64? It means that you can only disable public network access for an [#Azure](https://mastodon.social/tags/Azure) API Management service after you created a Private Endpoint, which is a separate resource and itself depends on the API Management service for creation. So you can't make the service private until after initial deployment (which we already discovered on day 55).

[View post](https://mastodon.social/@azureshit/110456731708653972)

---

## 2023-05-26T12:53:18.298Z

Day 65. For your [#Azure](https://mastodon.social/tags/Azure) Logic App, you can use a Storage Account without public network access and with a Private Endpoint to store your app's artifacts. However, you can only deploy such a constellation over ARM templates. Want to use the Azure Portal or [#Terraform](https://mastodon.social/tags/Terraform)? Then you can only restrict public access to the Storage Account after you have already deployed it. Good luck automating your infrastructure on Azure.

[View post](https://mastodon.social/@azureshit/110435080489922441)

---

## 2023-05-25T07:57:14.693Z

Day 64. Not supported if the [#Azure](https://mastodon.social/tags/Azure) API Management service does not at least what?

[View post](https://mastodon.social/@azureshit/110428254023522168)

---

## 2023-05-24T09:32:20.065Z

Day 63. To work around the issue with Azure's own reference architetcure from day 61, you need to use a custom DNS resolver that is able to look up DNS records on fallback DNS servers if the server with the matching DNS zone does not return any results. The managed [#Azure](https://mastodon.social/tags/Azure) Private DNS Resolver is unable to do so and thereby breaks Azure's own DNS concepts.

[View post](https://mastodon.social/@azureshit/110422965620721599)

---

## 2023-05-23T07:34:14.682Z

Day 62. Remember the broken built-in [#Azure](https://mastodon.social/tags/Azure) policy from day 8? There are actually even more PaaS services where public network access does not get denied even though the policy advertises to do so. Azure Logic Apps with a Windows App Service plan with public access enabled do not get denied by said policy.

[View post](https://mastodon.social/@azureshit/110416838961423352)

---

## 2023-05-22T08:16:34.718Z

Day 61. The [#Azure](https://mastodon.social/tags/Azure) Cloud Adoption Framework's reference architecture on Private Link and DNS integration at scale intends for you to create central Private Link DNS zones where the DNS records for all PaaS resources get maintained. However, once you do this, you are effectively blocking yourself from accessing all external PaaS resources that internally use Private Endpoints themselves, because now all \*.privatelink.\* hostnames get only resolved within your own Private Link zones.

[View post](https://mastodon.social/@azureshit/110411343116036625)

---

## 2023-05-21T21:09:14.648Z

Day 60. If the [#Azure](https://mastodon.social/tags/Azure) [#Terraform](https://mastodon.social/tags/Terraform) provider wants do delete a VM Scale Set, it will try to scale down the amount of instances to 0. But apparently scaling down does not work if there is no capacity left in the respective availability zones. No wonder Azure has capacity problems if they don't allow you to let go of existing resources.

[View post](https://mastodon.social/@azureshit/110408719049861610)

---

## 2023-05-19T09:02:38.767Z

Day 59. Not Azure, but related to the tech stack of hell: Minor shit like this is what makes all of these shitty products not fun to use. They can't even get text alignment right in Teams.

[View post](https://mastodon.social/@azureshit/110394537329668664)

---

## 2023-05-18T08:42:39.706Z

Day 58. Create commands in the Azure CLI are per default idempotent, meaning you can run them for resources that already exist and you will simply retrieve the current resource. But if you re-create an already existing management group, the CLI will tell you that it does not have any children, even though it did before and still does.

[View post](https://mastodon.social/@azureshit/110388796437565938)

---

## 2023-05-17T08:20:53.931Z

Day 57. Azure has had capacity problems for the past few weeks now. Most locations in Europe we are trying to deploy resources to do not have any more capacity to provision even the smallest VM scale sets. This is an ongoing issue and forces us to regularly move between locations with both testing and prod environments.

[View post](https://mastodon.social/@azureshit/110383048552014348)

---

## 2023-05-16T07:48:51.289Z

Day 56. Registering a provider through the Azure CLI regularly fails with an Internal Server Error.

[View post](https://mastodon.social/@azureshit/110377260239347118)

---

## 2023-05-15T09:12:17.836Z

Day 55. You can disable public network access for Azure API Management service instances, but only after you have already deployed them.

[View post](https://mastodon.social/@azureshit/110371926038047379)

---

## 2023-05-12T08:11:16.172Z

Day 54. The Azure CLI does not know your subscriptions in realtime. After creating a new subscription, it takes a wild mix of updating your global subscriptions filter (btw, what a shitty concept), refreshing the CLI's subscription list and furiously logging out and in again in the CLI until your missing subscription finally shows up. We still haven't figured out a reliable way to do this. Of all the Azure shit so far, the randomness here makes this by far the most frustrating shit.

[View post](https://mastodon.social/@azureshit/110354699135953818)

---

## 2023-05-11T06:50:02.993Z

Day 53. Remember the soft-deleted Azure API Management services from day 50? According to the docs, the Azure Terraform provider will recover soft-deleted instances automatically when trying to create a new one with the same name, but that always fails because "it is unable to undelete the service".

[View post](https://mastodon.social/@azureshit/110348717456842109)

---

## 2023-05-10T07:41:21.862Z

Day 52. Azure API Management exposes a default health check endpoint under /status-0123456789abcdef.

[View post](https://mastodon.social/@azureshit/110343256923248922)

---

## 2023-05-09T07:20:35.247Z

Day 51. Management locks on a route prevent both the route and the parent route table from getting deleted. But instead you can simply perform a PUT request on the route table and overwrite the routes with an empty array. All routes are then deleted, while the management locks for the routes still exist.

[View post](https://mastodon.social/@azureshit/110337512914665224)

---

## 2023-05-08T12:41:39.022Z

Day 50. Soft-deleted Azure API Management services can only be restored by performing a PUT request to ARM overwriting the resource and setting a restore property to true. You can't do it over the CLI or anyway else, and if you do it over the API, the restore still requires full 50 minutes. That's excatly how long a new deployment would take.

[View post](https://mastodon.social/@azureshit/110333113075152863)

---

## 2023-05-06T09:18:32.502Z

Day 49. The Azure Portal shows you both the Public and the Private IP address for your Azure API Management service in one field. If you click "copy to clipboard", it copies the whole field. The text is not selectable and if you click on the hyperlink, it directs you to some docs. The fastest way to copy one IP address is literally to just type it by hand.

[View post](https://mastodon.social/@azureshit/110320989798422633)

---

## 2023-05-05T08:48:56.397Z

Day 48. Oh no, the diagnostic settings do not support diagnostic settings.

[View post](https://mastodon.social/@azureshit/110315211089286168)

---

## 2023-05-04T08:28:28.804Z

Day 47. If for some reason you mess up your Azure API Management setup and Azure cannot reach your service's management endpoint, the Azure Portal will conveniently remind you of that every few minutes. Even if you aren't doing anything related to API Management at all.

[View post](https://mastodon.social/@azureshit/110309468327428246)

---

## 2023-05-03T06:38:29.849Z

Day 46. Haven't seen enough of Azure resource consistency? When dealing with child resources of Azure API Management in Terraform, some resources require you to specify the ID of the parent API Management service (such as the azurerm\_api\_management\_policy resource), while some want you to provide the service's name (such as the azurerm\_api\_management\_logger resource).

[View post](https://mastodon.social/@azureshit/110303373547819349)

---

## 2023-05-02T11:11:07.938Z

Day 45. Apparently Azure failed to update settings.

[View post](https://mastodon.social/@azureshit/110298783280671742)

---

## 2023-04-28T10:03:41.096Z

Day 44. If you try to create new role assignments in the Azure Portal, you can only search for principals with a search term that matches the starting letters of to the principal's name. For example, you would not find the principal "az-sp-terraform" by searching for "terraform".

[View post](https://mastodon.social/@azureshit/110275868825545589)

---

## 2023-04-27T08:07:49.683Z

Day 43. Azure API Management is a Private Link-supported PaaS service, but if you add a Private Endpoint to your API Management service, it can only be used for inbound traffic and there is no way to manage outbound traffic. Meaning you can make your instance accessible through a private network, but then it could only connect to your backend services through the Internet. What an exceptionally weird use case.

[View post](https://mastodon.social/@azureshit/110269750947416499)

---

## 2023-04-26T11:13:51.326Z

Day 42. It takes around 50 minutes to deploy an Azure API Management service instance.

[View post](https://mastodon.social/@azureshit/110264820126555570)

---

## 2023-04-25T08:23:30.170Z

Day 41. Deploying an Azure Kubernetes Service instance often fails with an Internal Server Error.

[View post](https://mastodon.social/@azureshit/110258487962388811)

---

## 2023-04-24T08:42:06.170Z

Day 40. When creating an Azure policy resource exemption (for example for a deny creation policy), you can only create it with a scope for a resource that already exists. Think about that.

[View post](https://mastodon.social/@azureshit/110252898790189251)

---

## 2023-04-17T08:29:48.423Z

Day 39. What you can see here is Schrödinger's lifecycle of updating an Azure resource: Started, Accepted and then both Failed and Succeeded.

[View post](https://mastodon.social/@azureshit/110213214268465169)

---

## 2023-04-16T03:46:49.803Z

Day 38. Error: An exception was thrown. Thanks, Azure.

[View post](https://mastodon.social/@azureshit/110206439247200318)

---

## 2023-04-14T13:05:41.183Z

Day 37. Creating such an Azure Cosmos DB account from day 36 through the Azure Terraform provider will result in Terraform exiting with an error. But the resource still gets created and subsequent Terraform runs will fail because a resource with the same ID already exists and needs to be imported. But guess what? You cannot import the Cosmos DB account due to it being "failed".

[View post](https://mastodon.social/@azureshit/110197312138871350)

---

## 2023-04-13T11:20:11.843Z

Day 36. Creation of Azure Cosmos DB accounts in some specific constellation will result in the resource being in a failed provisioning state. But the Azure portal does not give you any more information than "Failed". Good luck debugging.

[View post](https://mastodon.social/@azureshit/110191235028858538)

---

## 2023-04-12T08:00:18.932Z

Day 35. You can use az account set --name to set a default subscription context for your Azure CLI, but this context will be reset in case you log out and in again. Which is something you might need to do frequently if your Azure tenant's AD invalidates your refresh tokens regularly. This actually makes sense when you think about how they implemented subscriptions within the CLI, but is just a dumb concept in the first place. Luckily, there are other ways to set your default subscription.

[View post](https://mastodon.social/@azureshit/110184786751102591)

---

## 2023-04-11T13:56:14.527Z

Day 34. Seems like Azure engineers started "helping out" on Microsoft Office 365 products. The OneDrive web app is just as reliable in showing content as the Azure portal is.

[View post](https://mastodon.social/@azureshit/110180524000942758)

---

## 2023-04-04T07:50:03.602Z

Day 33. When you have multiple Private Endpoints for the same Private Link-supported Azure PaaS resource and they are linked to the same Private Link DNS Zone, all Private Endpoints manage the same DNS record within that zone. But if you delete one of the endpoints, the DNS record will be deleted as well, even though there are still corresponding Private Endpoints.

[View post](https://mastodon.social/@azureshit/110139447937947915)

---

## 2023-04-03T10:42:47.664Z

Day 32. Back with another installment of naming consistency in Azure: When querying the around 250 Azure providers, you will notice that the name of a handful of them is all lowercase for some weird reason. And then there's also "NGINX.NGINXPLUS".

[View post](https://mastodon.social/@azureshit/110134464850341695)

---

## 2023-03-31T13:45:49.167Z

Day 31. The Azure portal shows you costs by resource for your subscription, but somehow lists both the resource "virtualmachines" and individual virtual machines.

[View post](https://mastodon.social/@azureshit/110118197602810528)

---

## 2023-03-30T08:52:31.597Z

Day 30. When trying to rename an Azure subscription through the Azure Management API and using the latest API version available according to the docs, Azure will tell you that the API version is invalid. If you try one of the versions it tells you are supported, suddenly no matching HTTP resource can be found.

[View post](https://mastodon.social/@azureshit/110111382018146401)

---

## 2023-03-28T13:52:39.432Z

Day 29. Deleting a route and then making configuration changes on the route table will make the route come back from the dead. This is not a visualization problem, the route actually exists. It's due to the Azure portal somehow not realizing that the route has been deleted and just performing a PUT request on the whole route table resource, thereby overwriting the new routes array.

[View post](https://mastodon.social/@azureshit/110101237558814008)

---

## 2023-03-27T08:51:39.243Z

Day 28. Updating Azure Firewall policy rules can randomly result in the whole Firewall policy being in a failed provisioning state. There is no way to repair the policy besides deleting and re-creating it, and the Microsoft support is either unwilling or unable to fix this problem. Imagine this being a production workload.

[View post](https://mastodon.social/@azureshit/110094391655898653)

---

## 2023-03-26T12:57:19.070Z

Day 27. When creating an Azure Firewall and Firewall policy rules through the Azure Terraform provider, the creation of the rules will always fail for the same weird reason. And trying to run Terraform again will then fail because it is unable to create the rules due to a resource with the same ID already existing. This happens 100% of the time and always requires manual intervention to import the resource. Good luck trying to automate your infrastructure on Azure.

[View post](https://mastodon.social/@azureshit/110089695334806987)

---

## 2023-03-25T12:07:12.264Z

Day 26. When updating policies, your shiny cleaned up policy definition is not allowed to have less parameters than the previous one. You must manually delete the policy definition and then re-create it instead. How great, especially when trying to automate infrastructure.

And as usual there exists a GitHub issue for this which Microsoft decided to close without providing any real answer or fix.

[View post](https://mastodon.social/@azureshit/110083835970335029)

---

## 2023-03-24T07:20:48.332Z

Day 25. When deploying an Azure App Configuration instance which gets denied by policies, the logs tell you to see the details for more information but don't actually show you any more details besides "Validation failed".

[View post](https://mastodon.social/@azureshit/110077047493279129)

---

## 2023-03-23T09:19:25.634Z

Day 24. Azure is known for its descriptive error codes, such as "AzureFirewallDNSConfigNotAllowedForVhubOrVnetWithPolicy". But not this time. Imagine having thousands of lines of Terraform code and stumbling over this gem of an error message, which does not even give you the affected resource.

[View post](https://mastodon.social/@azureshit/110071851622861913)

---

## 2023-03-22T08:24:48.347Z

Day 23. Manually scaling up an Azure Scale Set from one instance to two instances will create two additional instances, from which one instantly gets deleted after its boot.

[View post](https://mastodon.social/@azureshit/110065974532228319)

---

## 2023-03-21T08:43:22.628Z

Day 22. Azure policies only get evaluated when Azure processes a request for the specified resource type. But some resources can be created both standalone or as in-line resources defined within another resource. For example, creating a route table with in-line routes won't trigger a policy that is supposed to deny specific routes. This makes it much more complicated to prevent or audit specifc resource constellations.

[View post](https://mastodon.social/@azureshit/110060385247390894)

---

## 2023-03-20T11:30:40.309Z

Day 21. Your Azure policy does not show compliance details? No worries, you just need to "wait an appropriate amount of time".

[View post](https://mastodon.social/@azureshit/110055380766419013)

---

## 2023-03-19T14:06:37.586Z

Day 20. Using the Microsoft Graph API to create Outlook calendar events with an open extension (which is different from a schema extension) always results in an Internal Server Error, but the event still gets created.

[View post](https://mastodon.social/@azureshit/110050331694571309)

---

## 2023-03-18T18:41:45.073Z

Day 19. The order of Azure Activity Logs is either completely random or based on an advanced and mysterious algorithm humankind yet has to understand.

[View post](https://mastodon.social/@azureshit/110045751218794417)

---

## 2023-03-17T09:30:36.549Z

Day 18. (DISPROVED: trailing commas are in fact not RFC 8259 compliant) Your Azure policy rule definition - which is supposed to be JSON - might be RFC 8259 compliant, but Azure does not care about that. It's not able to handle a trailing comma after the last array value.

[View post](https://mastodon.social/@azureshit/110037921729621711)

---

## 2023-03-16T10:53:31.308Z

Day 17. Not really Azure, but Microsoft Graph API. You can create schema extensions that extend the data model of the API to store custom attributes. Sounds great, until you learn that these extensions are public and anyone can see your data model now.

Interested in who is using Microsoft products for what? Just crawl the public API and you will find data model extensions of organizations such as Miele and Lambton College.

[View post](https://mastodon.social/@azureshit/110032585445056817)

---

## 2023-03-15T10:20:57.736Z

Day 16. When using Azure Privileged Identity Management to elevate to a privileged group, the Azure portal tells you that don't have to sign out and back in again. That is a lie. You have to do exactly that for your new permissions to populate.

[View post](https://mastodon.social/@azureshit/110026795105386324)

---

## 2023-03-14T11:34:00.383Z

Day 15. The admin user of an Azure VM is not allowed to be named John.

[View post](https://mastodon.social/@azureshit/110021420015918926)

---

## 2023-03-13T09:53:55.466Z

Day 14. When creating role assignments, the Azure Terraform provider prefixes role definition IDs with the targeted scope, while the Azure portal does not. The latter form of role defintion IDs isn't documented anywhere and means you have to inspect the network traffic from the Azure portal to the Azure Batch Service API (which is different from the Azure Management REST API) to figure out why your policy to deny specific role assignments does not work for all frontends.

[View post](https://mastodon.social/@azureshit/110015364167386241)

---

## 2023-03-12T11:30:24.569Z

Day 13. It takes nearly 7 minutes to delete a custom role definition through the Azure Terraform provider.

[View post](https://mastodon.social/@azureshit/110010081251493657)

---

## 2023-03-11T13:37:57.443Z

Day 12. For those who are being used to coherent cloud products and are wondering what the difference between role permissions and role actions is: Actions are part of the role's permissions and permissions can apparently also include "not actions" and other stuff. Well, at least sometimes. The data model somehow changes depending on the frontend you use.

[View post](https://mastodon.social/@azureshit/110004920479931338)

---

## 2023-03-10T08:49:08.617Z

Day 11. Back with yet another installment of eventual resource consistency at Azure. When trying to create both a custom role definition and a role assignment for said role, the Azure Terraform provider will fail to create the assignment after creating the definition, because it "could not find the role". It magically works on the second run though.

[View post](https://mastodon.social/@azureshit/109998122507726078)

---

## 2023-03-09T08:59:21.238Z

Day 10. Remember the weird Terraform behavior for VM Scale Sets from day 3? It actually applies to Scale Set Extensions as well. When executing a custom script through an extension and the command fails, Terraform will fail to create the resource. However, the extension has been created in Azure. Re-applying Terraform will fail because a resource with the same ID alredy exists.

[View post](https://mastodon.social/@azureshit/109992500345990982)

---

## 2023-03-08T09:22:19.308Z

Day 9. You can use Scale Set Extensions to apply commands as rolling upgrades to your VM instances. But don't you dare trying to give the resource a name other than "CustomScript" additionally to already specifying type "CustomScript", otherwise the Azure Terraform Provider will throw you an "ExtensionNotFoundForCPUArchitecture" error. You think this behavior is documented in the Terraform docs? It isn't.

[View post](https://mastodon.social/@azureshit/109986928348852861)

---

## 2023-03-07T11:08:05.911Z

Day 8. Think you can rely on Azure built-in policies to protect your infrastructure? You can't.

The built-in policy "Service Bus Namespaces should disable public network access" is not actually capable of denying creation of said resources with public access. Only after disabling public access on the resource and re-enabling it again, the policy somehow gets evaluated.

[View post](https://mastodon.social/@azureshit/109981681968647975)

---

## 2023-03-06T09:09:49.600Z

Day 7. Back with another installment of: Product behavior changes for no reason when switching to a different pricing tier. Azure Public IP addresses in Standard SKU deny all inbound traffic when used as frontend. They call it "secure by default". Azure, does this mean your Public IP Basic SKU is insecure by default?

[View post](https://mastodon.social/@azureshit/109975554595128429)

---

## 2023-03-05T14:29:46.428Z

Day 6. We are getting haunted by a ghost subnet. On multiple environments the Azure Terraform provider refuses to create this subnet that allegedly already exists, but when you ask the Azure CLI, there's nothing there.

[View post](https://mastodon.social/@azureshit/109971150368080778)

---

## 2023-03-04T09:43:42.446Z

Day 5. It takes full 20 minutes to deploy an Azure Cache for Redis instance through the Azure Terraform provider.

[View post](https://mastodon.social/@azureshit/109964363198912706)

---

## 2023-03-03T09:04:10.776Z

Day 4. Remember the Marketplace agreements from day 2? You can actually agree to any plan in these agreements, even to those that don't exist.

[View post](https://mastodon.social/@azureshit/109958545458834456)

---

## 2023-03-02T07:47:54.021Z

Day 3. When deploying a Scale Set with a rolling upgrade policy that requires the instances to be healthy after the upgrade, the Azure Terraform provider will fail to create the resource when the instances do not become healthy. But guess what? The Scale Set has been created in Azure. Re-applying Terraform will now result in an error, because - oh wonder - a resource with the same ID already exists.

[View post](https://mastodon.social/@azureshit/109952583206187506)

---

## 2023-03-01T08:37:57.474Z

Day 2. Ever wondered what the difference between "agreeing to an Azure Marketplace agreement" and "enabling programmatic deployments for offerings on a subscription" is? Easy, none. It's the same thing, just named differently in different frontends.

And of course Azure wouldn't document that minor inconsistency anywhere. Why should they? To help users understand their products?

[View post](https://mastodon.social/@azureshit/109947117730089717)

---

## 2023-02-28T11:34:21.302Z

Day 1. Scale Set VMs trying to issue a SSL certificate through DNS-01 with Azure DNS failing on startup. Turns out Azure Management API randomly returns 403, sometimes on DNS zone lookup, sometimes on record creation. Magically worked again after 2 hours of debugging and changing exactly nothing. Imagine this being a production workload.

[View post](https://mastodon.social/@azureshit/109942149040551717)

---

