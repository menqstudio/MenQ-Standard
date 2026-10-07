// MenQ Studio Design Standards — window.MenQ (React 18). Source: BroPS src/components/ui.tsx + MenQ additions.
import type React from 'react';
type Node = React.ReactNode;
export type Tone = 'neutral' | 'accent' | 'success' | 'warning' | 'danger' | 'info';
export type Status = 'online' | 'busy' | 'offline' | 'error';
export interface ButtonProps { children: Node; variant?: 'default' | 'primary' | 'danger' | 'ghost'; small?: boolean; loading?: boolean; disabled?: boolean; type?: 'button' | 'submit'; title?: string; onClick?: () => void; }
export interface CardProps { children: Node; className?: string; style?: React.CSSProperties; }
export interface PanelProps { title?: string; actions?: Node; children: Node; }
export interface PageHeaderProps { title: string; subtitle?: string; actions?: Node; }
export interface BadgeProps { children: Node; tone?: Tone; }
export interface StatusDotProps { status: Status; label?: string; }
export interface AvatarProps { name: string; kind?: 'bro' | 'agent'; }
export interface FieldProps { label: string; children: Node; }
export type InputProps = React.InputHTMLAttributes<HTMLInputElement> & { invalid?: boolean };
export interface FormRowProps { label: string; error?: string; children: Node; }
export interface TabsProps { items: { value: string; label: string; count?: number }[]; defaultValue?: string; value?: string; onChange?: (v: string) => void; }
export interface EmptyStateProps { title: string; hint?: string; glyph?: string; action?: Node; }
export interface SkeletonProps { rows?: number; }
export interface ToastProps { children: Node; tone?: 'success' | 'info' | 'error'; onDismiss?: () => void; }
export interface ModalProps { title: string; onClose?: () => void; inline?: boolean; children: Node; }
export interface ConfirmDialogProps { title: string; message: string; confirmLabel: string; cancelLabel: string; onConfirm?: () => void; onCancel?: () => void; inline?: boolean; }
export interface DrawerProps { title: string; onClose?: () => void; inline?: boolean; children: Node; }
export interface KpiStatProps { label: string; value: number; unit?: string; delta?: number; deltaLabel?: string; locale?: string; }
export interface TableProps<R = Record<string, unknown>> { columns: { key: string; label: string; align?: 'left' | 'right' | 'center'; render?: (row: R) => Node }[]; rows: R[]; caption?: string; }
export interface TimelineProps { items: { title: string; meta?: string; detail?: Node; state?: 'done' | 'running' | 'waiting' | 'failed' | 'pending' }[]; }
export interface ChatMessageProps { role?: 'human' | 'bro' | 'agent'; author: string; children: Node; time?: string; scope?: string; state?: 'running' | 'done' | 'failed'; stateLabel?: string; mine?: boolean; }
export interface AgentCardProps { name: string; role?: string; status: Status; statusLabel?: string; scope?: string[]; task?: string; taskLabel?: string; progress?: number; }
export interface ApprovalCardProps { title: string; risk?: 'low' | 'medium' | 'high'; riskLabel?: string; kicker?: string; description?: string; requestedBy?: string; approveLabel?: string; rejectLabel?: string; onApprove?: () => void; onReject?: () => void; }
export interface CommandComposerProps { onSubmit?: (text: string) => void; placeholder?: string; hint?: string; sendLabel?: string; label?: string; }
