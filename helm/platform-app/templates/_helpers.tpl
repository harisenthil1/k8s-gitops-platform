{{- define "platform-app.name" -}}
platform-app
{{- end }}

{{- define "platform-app.fullname" -}}
{{ .Release.Name }}
{{- end }}

{{- define "platform-app.labels" -}}
app.kubernetes.io/name: {{ include "platform-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
