variable "app_name" {
  type        = string
  description = "Application Name"
  default     = "retail-etl"
}

variable "container_cpu" {
  description = "Container cpu"
  default     = "2000m"
}

variable "container_memory" {
  description = "Container memory"
  default     = "2G"
}

variable "project_id" {
  type        = string
  description = "The name of the project"
  default     = "online-retail-etl"
}

variable "region" {
  type        = string
  description = "The default compute region"
  default     = "us-west1"
}

variable "zone" {
  type        = string
  description = "The default compute zone"
  default     = "us-west1-a"
}

variable "repository" {
  type        = string
  description = "The name of the Artifact Registry repository to be created"
  default     = "mage-data-prep"
}

variable "docker_image" {
  type        = string
  description = "The docker image to deploy to Cloud Run."
  default     = "mageai/mageai:latest"
}

variable "domain" {
  description = "Domain name to run the load balancer on. Used if `ssl` is `true`."
  type        = string
  default     = ""
}

variable "ssl" {
  description = "Run load balancer on HTTPS and provision managed certificate with provided `domain`."
  type        = bool
  default     = false
}

variable "credentials" {
  description = "credentials path for GCP"
  type        = string
  default     = "./.keys/online-retail-etl-401c33da4926.json"
}